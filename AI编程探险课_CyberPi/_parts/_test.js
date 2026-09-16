const fs = require("fs");
const base = __dirname;

function makeEl(id){
  return {
    _id: id, _html: "", _text: "", style: { setProperty: function(){} },
    classList: { toggle: function(){}, add: function(){}, remove: function(){} },
    setAttribute: function(){}, getAttribute: function(){ return null; },
    set innerHTML(v){ this._html = v; }, get innerHTML(){ return this._html; },
    set textContent(v){ this._text = String(v); }, get textContent(){ return this._text; },
    appendChild: function(){}, focus: function(){}, disabled: false
  };
}
const els = {};
global.window = { addEventListener: function(){} };
global.document = {
  addEventListener: function(){},
  getElementById: function(id){ if(!els[id]) els[id] = makeEl(id); return els[id]; },
  querySelector: function(sel){ return makeEl(sel); },
  querySelectorAll: function(){ return []; }
};
let store = {};
global.localStorage = { getItem: function(k){ return store[k] || null; }, setItem: function(k,v){ store[k]=v; }, removeItem: function(k){ delete store[k]; } };
global.location = { hash: "#/course/1" };
global.confirm = function(){ return false; };

let src = "";
["data1.js","data2.js","data3.js","data4.js"].forEach(f => src += fs.readFileSync(base + "\\" + f, "utf8") + "\n");
src += fs.readFileSync(base + "\\app.js", "utf8") + "\n";
eval(src);

// 模拟所有主要渲染路径
const results = [];
function check(name, cond){ results.push((cond ? "PASS " : "FAIL ") + name); }

check("ALL=32", ALL.length === 32);
check("quiz=96", ALL.reduce((n,l)=>n+l.quiz.length,0) === 96);

renderCourse(1);
let panelsHtml = els["coursePanels"]._html;
check("course1 intro has story", /小侦探找线索/.test(panelsHtml));
check("course1 blocks", /本课积木程序/.test(panelsHtml));
check("course1 task", /AI硬件编程任务/.test(panelsHtml));
check("course1 challenge", /挑战/.test(panelsHtml));
check("course1 quiz", /随堂问答/.test(panelsHtml));
check("course tabs 6", els["courseTabs"]._html.includes("学习目标"));

// 问答流程：课程1 quiz 共3题，先答错再答对，然后下一题
quizState.idx = 0; quizState.correct = 0; quizState.wrong = 0; quizState.firstTry = 0;
renderQuiz();
let q1 = COURSE[1].quiz[0];
const optBtns = [];
for(let i=0;i<q1.o.length;i++){ optBtns.push(makeEl("opt"+i)); }
// 模拟点错选项
let wrongBtn = optBtns[(q1.a + 1) % q1.o.length];
wrongBtn.getAttribute = function(){ return String((q1.a + 1) % q1.o.length); };
els["quizCard"].querySelectorAll = function(){ return optBtns; };
answerQuiz(wrongBtn);
check("wrong increments", quizState.wrong === 1);
// 点对
let rightBtn = optBtns[q1.a];
rightBtn.getAttribute = function(){ return String(q1.a); };
rightBtn.classList = { add: function(){}, contains: function(){ return false; }, remove: function(){} };
els["quizCard"].querySelectorAll = function(){ return optBtns; };
answerQuiz(rightBtn);
check("correct increments", quizState.correct === 1 && quizState.firstTry === 1);
nextQuiz();
check("advanced to q2", quizState.idx === 1);

// 快进到最后一题并完成
quizState.idx = 2;
renderQuiz();
let q3 = COURSE[1].quiz[2];
let b3 = optBtns[q3.a];
b3.getAttribute = function(){ return String(q3.a); };
b3.classList = { add: function(){}, contains: function(){ return false; }, remove: function(){} };
els["quizCard"].querySelectorAll = function(){ return optBtns; };
answerQuiz(b3);
check("q3 correct", quizState.correct === 2);
nextQuiz();
check("finish records done", (DB.get().records["1"] || {}).done === true);

renderHardware();
check("hardware svg", els["hwSvgCard"]._html.includes("五向摇杆"));
check("hardware info", els["hwInfo"]._html.includes("1.44 英寸"));

renderGrowth();
check("growth ring", els["growPct"]._text === "3%"); // 32 课完成 1 课 → 3%
check("growth badges", els["badgeGrid"]._html.includes("初来乍到"));

renderHome();
check("home chapters", els["chapters"]._html.includes("第 01 课"));
check("path svg", els["pathSvg"]._html.includes("path-lesson"));

// 全部 32 课渲染一遍
let bad = 0;
for(let i=1;i<=32;i++){
  renderCourse(i);
  let ph = els["coursePanels"]._html;
  if(!COURSE[i] || ph.length < 50 || !ph.includes("AI硬件编程任务")){ bad++; }
}
check("all 32 courses render", bad === 0);

console.log(results.join("\n"));
console.log(results.some(r=>r.startsWith("FAIL")) ? "TEST FAIL" : "TEST ALL PASS");
