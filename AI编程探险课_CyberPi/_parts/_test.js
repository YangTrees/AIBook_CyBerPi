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
["data1.js","data2.js","data3.js","data4.js","refinements.js"].forEach(f => src += fs.readFileSync(base + "\\" + f, "utf8") + "\n");
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
const course1Text = JSON.stringify(COURSE[1]) + panelsHtml;
check("course1 follows mBlock CyberPi flow", /mBlock/.test(course1Text) && /设备已连接/.test(course1Text) && /实体按钮 A/.test(course1Text));
check("course1 has no green-flag stage flow", !/绿旗|角色项目|在线积木编程舞台|先在舞台/.test(course1Text));
check("course1 uses real CyberPi input", COURSE[1].blocks.some(function(b){ return b[0] === "事件" && /CyberPi|按钮|按键/.test(b[1]); }));
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
let missingFlow = 0;
let missingInput = 0;
let missingOutput = 0;
let staleStageFlow = 0;
let badStepCount = 0;
let vagueSteps = 0;
let missingValidation = 0;
let missingMedia = 0;
let missingTaskDetail = 0;
let missingScreenshotFiles = 0;
let missingRefinement = 0;
let repeatedProgramTask = 0;
let weakProgramExplanation = 0;
for(let i=1;i<=32;i++){
  renderCourse(i);
  let ph = els["coursePanels"]._html;
  if(!COURSE[i] || ph.length < 50 || !ph.includes("AI硬件编程任务")){ bad++; }
  if(!ph.includes("本课统一实施流程") || !ph.includes("设备已连接") || !ph.includes("真实输入—逻辑处理—硬件输出") || !ph.includes("真机验收")){ missingFlow++; }
  let cats = COURSE[i].blocks.map(function(b){ return b[0]; });
  if(!cats.some(function(c){ return ["事件","传感","网络/AI","扩展"].includes(c); })){ missingInput++; }
  if(!cats.some(function(c){ return ["显示","外观","灯","声音","运动"].includes(c); })){ missingOutput++; }
  if(/绿旗|在线积木编程舞台|在线编程角色|在舞台上|角色显示识别类别/.test(JSON.stringify(COURSE[i]))){ staleStageFlow++; }
  if(!Array.isArray(COURSE[i].steps) || COURSE[i].steps.length !== 5){ badStepCount++; }
  if(COURSE[i].steps.filter(function(s){ return /拖入|建立|新建|准备|按|读取|显示|设置|输入|运行|训练|采集|比较|记录|上传|测试|验证|观察|修改|加入|完成|自制|计算|绘制|切换|调用|检查|修复|调整|选择|试玩|辨认|对比/.test(s); }).length < 4){ vagueSteps++; }
  if(!/验证|测试|验收|复测|观察|比较|运行|试玩|检查|确认|辨认|对比/.test(COURSE[i].steps.join(''))){ missingValidation++; }
  let pad = i < 10 ? '0'+i : ''+i;
  if(!ph.includes('lesson-'+pad+'/full-program.png') || !ph.includes('lesson-'+pad+'/step-02.png') || !ph.includes('lesson-'+pad+'/step-03.png') || !ph.includes('lesson-'+pad+'/step-04.png') || !ph.includes('openImgLightbox')){ missingMedia++; }
  if(!ph.includes('今天要做出') || !ph.includes('选择你的挑战') || !ph.includes('试一试，找一找，再升级')){ missingTaskDetail++; }
  if(!COURSE[i].transfer || !Array.isArray(COURSE[i].transfer.steps) || COURSE[i].transfer.steps.length !== 5 || !ph.includes('举一反三')){ missingRefinement++; }
  if(COURSE[i].transfer && (COURSE[i].transfer.name === COURSE[i].projName || COURSE[i].transfer.eff === COURSE[i].projEff || COURSE[i].transfer.steps.join('') === COURSE[i].steps.join(''))){ repeatedProgramTask++; }
  if(!COURSE[i].programMeaning || COURSE[i].programMeaning.length < 30 || !COURSE[i].programObserve || !ph.includes('先玩明白，再动手搭') || !ph.includes('小眼睛看这里')){ weakProgramExplanation++; }
  ['full-program.png','step-02.png','step-03.png','step-04.png'].forEach(function(name){
    if(!fs.existsSync(base+'\\..\\assets\\blocks\\lesson-'+pad+'\\'+name)){ missingScreenshotFiles++; }
  });
}
check("all 32 courses render", bad === 0);
check("all courses show mBlock to CyberPi workflow", missingFlow === 0);
check("all courses have real input", missingInput === 0);
check("all courses have hardware output", missingOutput === 0);
check("all courses remove stale stage flow", staleStageFlow === 0);
check("all courses have exactly 5 detailed steps", badStepCount === 0);
check("all course steps are actionable", vagueSteps === 0);
check("all courses include validation", missingValidation === 0);
check("all courses render zoomable full and step screenshots", missingMedia === 0);
check("all courses have rich task and debugging sections", missingTaskDetail === 0);
check("all courses separate demonstration and transfer tasks", missingRefinement === 0 && repeatedProgramTask === 0);
check("all courses explain program meaning and observation focus", weakProgramExplanation === 0);
check("lesson 3 explains SOS before coding", /国际通用的求救信号/.test(COURSE[3].programMeaning) && /三个短信号/.test(COURSE[3].programMeaning));
check("lesson 1 uses child-facing program copy", /团团按一下 A/.test(COURSE[1].programHook) && /按钮 A → 数字加1/.test(COURSE[1].programWatch));
renderCourse(4);
const course4TaskHtml = els["coursePanels"]._html;
check("task steps use block colors without completion checkboxes", !course4TaskHtml.includes('□ 完成') && course4TaskHtml.includes('--step-color:') && course4TaskHtml.includes('step-block-tag'));
check("task levels use icons instead of character badges", course4TaskHtml.includes('aria-hidden="true"><svg') && !course4TaskHtml.includes('<i>必</i>') && !course4TaskHtml.includes('<i>星</i>') && !course4TaskHtml.includes('<i>创</i>'));
check("challenge panel uses child-friendly play flow", course4TaskHtml.includes('试玩、找错和升级') && course4TaskHtml.includes('先试一试') && course4TaskHtml.includes('不对就找一找') && course4TaskHtml.includes('改一处，再试一次'));
check("learning goals render once without repeated summary", (course4TaskHtml.split(COURSE[4].knowledge[0]).length - 1) === 1 && !course4TaskHtml.includes('kp-list') && !course4TaskHtml.includes('本课达成'));
check("program section presents a modular map", course4TaskHtml.includes('程序模块地图') && course4TaskHtml.includes('触发模块') && course4TaskHtml.includes('思考模块') && course4TaskHtml.includes('反馈模块'));
check("experiment record card was removed", !course4TaskHtml.includes('实验记录卡') && !course4TaskHtml.includes('运行前，我认为会'));
check("lesson 4 uses a visual variable warehouse", COURSE[4].projName === '团团的记忆仓库' && COURSE[4].blocks.some(function(b){ return b[0] === '自制'; }) && /库存柱/.test(COURSE[4].projEff));
check("targeted lessons use theme-matched modular programs", [5,7,11,12,14,16].every(function(id){ return COURSE[id].blocks.some(function(b){ return b[0] === '自制'; }); }) && /披萨/.test(COURSE[11].projName) && /对决/.test(COURSE[16].projName));
check("all 128 screenshot assets exist", missingScreenshotFiles === 0);

const shell = fs.readFileSync(base + "\\shell.html", "utf8");
check("image lightbox has zoom controls", /imgLightbox/.test(shell) && /changeImageZoom\(-\.25\)/.test(shell) && /changeImageZoom\(\.25\)/.test(shell) && /resetImageZoom/.test(shell));
check("image lightbox shows full step caption", /lightboxCaption/.test(shell));
check("step cards no longer use the distorted zoom glyph", !/⌕/.test(fs.readFileSync(base + "\\app.js", "utf8")));

console.log(results.join("\n"));
console.log(results.some(r=>r.startsWith("FAIL")) ? "TEST FAIL" : "TEST ALL PASS");
