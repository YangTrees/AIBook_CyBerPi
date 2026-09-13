/* ============ 章节元数据 ============ */
var CHAPTERS = [
  {id:1, name:'信息与感知', range:'第 1–8 课', desc:'呼应绘本模块A「信息从哪里来」+ 模块B「看见像素世界」', color:'var(--ch1)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>'},
  {id:2, name:'算法与思维', range:'第 9–16 课', desc:'呼应绘本模块C「机器按规则做事」+ 模块D「机器如何思考」', color:'var(--ch2)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 4h8M8 4a3 3 0 0 0-3 3v3a3 3 0 0 1-3 3 3 3 0 0 1 3 3v3a3 3 0 0 0 3 3M16 4a3 3 0 0 1 3 3v3a3 3 0 0 0 3 3 3 3 0 0 0-3 3v3a3 3 0 0 1-3 3"/></svg>'},
  {id:3, name:'机器学习', range:'第 17–24 课', desc:'呼应绘本模块E「从例子里学」+ 模块F「神经网络是什么」', color:'var(--ch3)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="6" r="2.4"/><circle cx="19" cy="6" r="2.4"/><circle cx="12" cy="18" r="2.4"/><path d="M6.8 7.4 10.8 16M17.2 7.4 13.2 16M7.4 6h9.2"/></svg>'},
  {id:4, name:'AI 创造与未来', range:'第 25–32 课', desc:'呼应绘本模块G「AI会说话会画画」+ 模块H「安全、偏见与未来」', color:'var(--ch4)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 4.6L18.5 9l-4.7 1.4L12 15l-1.8-4.6L5.5 9l4.7-1.4L12 3z"/><path d="M19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9L19 15z"/></svg>'}
];

/* ============ 课程数据汇总 ============ */
var ALL = [].concat(LESSONS_1, LESSONS_2, LESSONS_3, LESSONS_4);
var COURSE = {};
ALL.forEach(function(l){ COURSE[l.id] = l; });

/* 积木分类颜色 */
var CAT_COLOR = {事件:'var(--cat-event)',控制:'var(--cat-control)',显示:'var(--cat-display)',灯:'var(--cat-light)',声音:'var(--cat-sound)',传感:'var(--cat-sense)',运算:'var(--cat-op)',变量:'var(--cat-var)','网络/AI':'var(--cat-ai)',扩展:'var(--cat-ext)',自制:'var(--cat-my)'};

/* ============ 工具函数 ============ */
function $(s){ return document.querySelector(s); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function fmtNo(n){ return n < 10 ? '第 0'+n+' 课' : '第 '+n+' 课'; }
function chColor(ch){ return CHAPTERS[ch-1].color; }

/* ============ 存储 ============ */
var DB = {
  load: function(){ try{ return JSON.parse(localStorage.getItem('cyberpi_course')||'{}'); }catch(e){ return {}; } },
  save: function(d){ localStorage.setItem('cyberpi_course', JSON.stringify(d)); },
  get: function(){ var d = this.load(); d.nick = d.nick || ''; d.records = d.records || {}; return d; },
  lessonRec: function(d, id){ return d.records[id] || {done:false, correct:0, wrong:0}; },
  doneCount: function(d){ return Object.keys(d.records).filter(function(k){ return d.records[k].done; }).length; }
};

/* ============ 路由 ============ */
function go(hash){
  if(location.hash === hash){ route(); } else { location.hash = hash; }
}
function route(){
  var h = location.hash || '#/home';
  var m;
  if(h === '#/home' || h === '' || h === '#/'){ showView('view-home'); renderHome(); setNav('home'); window.scrollTo(0,0); }
  else if((m = h.match(/^#\/course\/(\d+)$/))){ showView('view-course'); renderCourse(parseInt(m[1],10)); setNav('course'); window.scrollTo(0,0); }
  else if(h === '#/hardware'){ showView('view-hardware'); renderHardware(); setNav('hardware'); window.scrollTo(0,0); }
  else if(h === '#/growth'){ showView('view-growth'); renderGrowth(); setNav('growth'); window.scrollTo(0,0); }
  else { location.hash = '#/home'; }
}
function showView(id){
  ['view-home','view-course','view-hardware','view-growth'].forEach(function(v){
    document.getElementById(v).style.display = (v === id) ? '' : 'none';
  });
}
function setNav(key){
  document.querySelectorAll('[data-nav]').forEach(function(el){
    el.classList.toggle('active', el.getAttribute('data-nav') === key);
  });
}

/* ============ 昵称 ============ */
function renderNick(){
  var d = DB.get();
  if(d.nick){
    document.getElementById('nickName').textContent = d.nick;
    document.getElementById('nickAvatar').textContent = d.nick.slice(0,1);
  } else {
    document.getElementById('nickName').textContent = '小探险家';
    document.getElementById('nickAvatar').textContent = '?';
  }
  if(!d.nick){ document.getElementById('nickOverlay').style.display = 'grid'; document.getElementById('nickInput').focus(); }
  else { document.getElementById('nickOverlay').style.display = 'none'; }
}
function openNick(){ document.getElementById('nickOverlay').style.display = 'grid'; setTimeout(function(){ document.getElementById('nickInput').focus(); }, 50); }
function saveNick(){
  var v = document.getElementById('nickInput').value.trim() || '小探险家';
  var d = DB.get(); d.nick = v; DB.save(d);
  renderNick();
}

/* ============ 首页 ============ */
function renderHome(){
  renderPathSvg();
  renderChapters();
  renderHomeStats();
}
function renderHomeStats(){
  var d = DB.get();
  var done = DB.doneCount(d);
  var items = [['32','节编程课'],['4','大学习章节'],['8','个 AI 主题'],['96','道随堂问答']];
  if(done > 0){ items[3] = [done + '/32', '已学课程']; }
  document.querySelector('.stats-bar').innerHTML = items.map(function(it){
    return '<div class="stat-card"><div class="num">'+it[0]+'</div><div class="lab">'+it[1]+'</div></div>';
  }).join('');
}

/* ---- 学习路径 SVG ---- */
function renderPathSvg(){
  var d = DB.get();
  var W = 1100, colX = [120, 398, 676, 954];
  var svg = '<svg class="path-svg" viewBox="0 0 '+W+' 300" role="img" aria-label="课程学习路径">';
  svg += '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#B9CBE4"/></marker></defs>';
  var i, k;
  for(i=0;i<3;i++){
    var x1 = colX[i]+78, x2 = colX[i+1]-78, cx = (x1+x2)/2;
    svg += '<path d="M'+x1+',46 C'+cx+',20 '+cx+',72 '+x2+',46" fill="none" stroke="#C6D6EC" stroke-width="3" stroke-dasharray="1 9" stroke-linecap="round" marker-end="url(#arrow)"/>';
  }
  CHAPTERS.forEach(function(ch, ci){
    var cx = colX[ci], c = ch.color;
    svg += '<g><circle cx="'+cx+'" cy="46" r="30" fill="'+c+'" opacity=".12"/>' +
      '<circle cx="'+cx+'" cy="46" r="24" fill="'+c+'"/>' +
      '<text x="'+cx+'" y="53" text-anchor="middle" font-size="15" font-weight="800" fill="#fff">'+ch.id+'</text>' +
      '<text x="'+cx+'" y="98" text-anchor="middle" font-size="15" font-weight="800" fill="#3d4b63">'+ch.name+'</text>' +
      '<text x="'+cx+'" y="116" text-anchor="middle" font-size="11.5" fill="#8b98ad" font-weight="600">'+ch.range+'</text></g>';
    var dx = [-36, 36];
    for(k=0;k<8;k++){
      var px = cx + dx[k%2], py = 150 + Math.floor(k/2)*38;
      var lid = (ch.id-1)*8 + k + 1;
      var rec = d.records[lid] || {};
      var done = rec.done;
      var fill = done ? 'var(--ok)' : (c+'22');
      var tx = done ? '#fff' : c;
      svg += '<g class="path-lesson" data-id="'+lid+'" onclick="go(\'#/course/'+lid+'\')" style="cursor:pointer">' +
        '<circle cx="'+px+'" cy="'+py+'" r="14" fill="'+fill+'" stroke="'+c+'" stroke-width="2"/>' +
        '<text x="'+px+'" y="'+(py+5)+'" text-anchor="middle" font-size="12" font-weight="800" fill="'+tx+'">'+lid+'</text>' +
        '<title>第'+lid+'课 · '+esc(COURSE[lid].title)+'</title></g>';
    }
  });
  svg += '</svg>';
  document.getElementById('pathSvg').innerHTML = svg;
}

/* ---- 章节 + 课程卡 ---- */
function renderChapters(){
  var d = DB.get();
  var html = '';
  CHAPTERS.forEach(function(ch){
    var list = ALL.filter(function(l){ return l.ch === ch.id; });
    var done = list.filter(function(l){ return (d.records[l.id]||{}).done; }).length;
    var pct = Math.round(done / 8 * 100);
    html += '<div class="chapter">' +
      '<div class="chapter-head" onclick="go(\'#/course/'+list[0].id+'\')">' +
        '<div class="ch-head-ico" style="background:'+ch.color+'">'+ch.icon+'</div>' +
        '<div class="ch-head-txt"><h3>'+ch.name+'</h3><p>'+ch.desc+'</p></div>' +
        '<div class="ch-head-meta" style="--ch-color:'+ch.color+'">'+done+' / 8 课完成<div class="pbar"><i style="width:'+pct+'%"></i></div></div>' +
      '</div><div class="lesson-grid">';
    list.forEach(function(l){
      var rec = d.records[l.id] || {};
      var pad = l.id < 10 ? '0' + l.id : '' + l.id;
      html += '<button class="lesson-card'+(rec.done?' done':'')+'" style="--ch-color:'+ch.color+'" onclick="go(\'#/course/'+l.id+'\')">' +
        '<div class="lc-cover"><img src="assets/lessons/'+pad+'.jpg" alt="'+esc(l.title)+'">' +
        '<span class="lc-no-badge">'+fmtNo(l.id)+'</span>' +
        '<span class="lc-check-badge"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5 9.5 18 20 6.5"/></svg></span></div>' +
        '<div class="lc-body">' +
        '<h4>'+esc(l.title)+'</h4>' +
        '<span class="lc-theme">'+esc(l.theme)+'</span>' +
        '<span class="lc-echo">呼应 第'+l.echoId+'课 · '+esc(l.echoTitle)+'</span>' +
        '<span class="lc-go">开始学习 <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>' +
        '</div></button>';
    });
    html += '</div></div>';
  });
  document.getElementById('chapters').innerHTML = html;
}

/* ============ 课程详情 ============ */
var TABS = [
  {key:'intro', name:'课程导入', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'},
  {key:'know', name:'AI 知识点', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 19.5a5.5 5.5 0 0 1-5.5-5.5V5h16v9a5.5 5.5 0 0 1-5.5 5.5h-5z"/><path d="M12 5v10"/></svg>'},
  {key:'blocks', name:'编程积木', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="12" height="10" rx="2.5"/><rect x="16.5" y="7" width="4.5" height="10" rx="2"/><path d="M9 7V5"/></svg>'},
  {key:'demo', name:'CyberPi 演示', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="12" rx="3"/><circle cx="12" cy="12" r="3.2"/><path d="M7 6V4h10v2"/></svg>'},
  {key:'challenge', name:'动手挑战', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 13.5H11L9.5 22 19 10h-6.5L13 2z"/></svg>'},
  {key:'quiz', name:'知识问答', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.4 2.3c-.8.3-.9 1-.9 1.7M12 17h.01"/></svg>'}
];
var quizState = null;

function renderCourse(id){
  var l = COURSE[id];
  if(!l){ go('#/home'); return; }
  var ch = CHAPTERS[l.ch-1];
  var d = DB.get();
  var rec = DB.lessonRec(d, id);

  document.getElementById('courseTop').style.setProperty('--ch-color', ch.color);
  document.getElementById('ctNo').textContent = fmtNo(id);
  document.getElementById('ctTitle').textContent = l.title;
  document.getElementById('ctSub').textContent = '第'+ch.id+'章 · '+ch.name+' ｜ '+l.theme;
  var pct = rec.done ? 100 : Math.round(rec.correct / l.quiz.length * 100);
  document.getElementById('ctRing').style.setProperty('--p', pct);
  document.getElementById('ctRingPct').textContent = rec.done ? '✓' : pct + '%';
  document.getElementById('ctProgTxt').textContent = rec.done ? '本课已完成' : '完成问答点亮进度';

  document.getElementById('courseTabs').innerHTML = TABS.map(function(t, i){
    return '<button class="tab-btn'+(i===0?' active':'')+'" data-tab="'+t.key+'" onclick="switchTab(this)">' +
      '<span class="t-ico" style="background:'+ch.color+'">'+t.icon+'</span>'+t.name+'</button>';
  }).join('');

  document.getElementById('coursePanels').innerHTML =
    panelIntro(l, ch) + panelKnow(l, ch) + panelBlocks(l, ch) + panelDemo(l, ch) + panelChallenge(l, ch) + panelQuiz(l, ch);

  var prev = id > 1 ? COURSE[id-1] : null;
  var next = id < 32 ? COURSE[id+1] : null;
  document.getElementById('lessonNav').innerHTML =
    (prev ? '<button class="ln-btn" onclick="go(\'#/course/'+prev.id+'\')"><span class="ln-t">上一课</span><span class="ln-c">'+fmtNo(prev.id)+' '+esc(prev.title)+'</span></button>' : '<div></div>') +
    (next ? '<button class="ln-btn next" onclick="go(\'#/course/'+next.id+'\')"><span class="ln-t">下一课</span><span class="ln-c">'+fmtNo(next.id)+' '+esc(next.title)+'</span></button>'
          : '<button class="ln-btn next" onclick="go(\'#/growth\')"><span class="ln-t">全部完成！</span><span class="ln-c">查看成长档案 →</span></button>');

  quizState = {id:id, idx:0, correct:0, wrong:0, firstTry:0, start:Date.now(), done:false};
  renderQuiz();
}
function switchTab(btn){
  document.querySelectorAll('#courseTabs .tab-btn').forEach(function(b){ b.classList.remove('active'); });
  btn.classList.add('active');
  var key = btn.getAttribute('data-tab');
  document.querySelectorAll('#coursePanels .tab-panel').forEach(function(p){ p.classList.remove('active'); });
  document.getElementById('panel-'+key).classList.add('active');
}

/* ---- 面板：课程导入 ---- */
function panelIntro(l, ch){
  var pad = l.id < 10 ? '0' + l.id : '' + l.id;
  var steps = [
    {ico:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>', t:'读故事', p:'回顾绘本第'+l.echoId+'课《'+l.echoTitle+'》'},
    {ico:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 9h.01M16 9h.01M8 15h8"/></svg>', t:'学知识', p:'掌握本节 AI 知识点'},
    {ico:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="12" rx="3"/><circle cx="12" cy="12" r="3.2"/><path d="M7 6V4h10v2"/></svg>', t:'做项目', p:'在 mBlock 搭积木，CyberPi 现场演示'}
  ];
  return '<div class="panel-card tab-panel active" id="panel-intro">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[0].icon+'</span>课程导入 · 绘本呼应</h3>' +
    '<div class="intro-hero">' +
      '<div class="intro-cover"><img src="assets/lessons/'+pad+'.jpg" alt="'+esc(l.title)+'"></div>' +
      '<div class="ih-info">' +
        '<h2>'+esc(l.title)+'</h2>' +
        '<div class="ih-theme">'+esc(l.theme)+' ｜ 第'+ch.id+'章 '+ch.name+'</div>' +
        '<div class="ih-desc">'+esc(l.echoBrief)+'</div>' +
      '</div>' +
    '</div>' +
    '<div class="echo-box">' +
      '<span class="e-tag">呼应绘本课 · 第'+l.echoId+'课《'+esc(l.echoTitle)+'》</span>' +
      '<div class="e-title">'+esc(l.echoBrief)+'</div>' +
      '<div class="e-story">'+esc(l.story)+'</div>' +
    '</div>' +
    '<div class="flow-steps">' + steps.map(function(s){
      return '<div class="flow-step"><div class="fs-ico">'+s.ico+'</div><b>'+s.t+'</b><p>'+s.p+'</p></div>';
    }).join('') + '</div></div>';
}

/* ---- 面板：AI 知识点 ---- */
function panelKnow(l, ch){
  return '<div class="panel-card tab-panel" id="panel-know">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[1].icon+'</span>本节 AI 知识点</h3>' +
    '<div class="kp-list">' + l.knowledge.map(function(k, i){
      return '<div class="kp-item"><span class="kp-no">'+(i+1)+'</span><p>'+esc(k)+'</p></div>';
    }).join('') + '</div></div>';
}

/* ---- 面板：编程积木 ---- */
function panelBlocks(l, ch){
  var rows = '';
  l.blocks.forEach(function(b){
    var color = CAT_COLOR[b[0]] || 'var(--primary)';
    rows += '<div class="blk-row"><span class="blk-lab">'+b[0]+'</span>' +
      '<span class="blk" style="background:'+color+'"><span class="blk-cat">'+b[0]+'</span>'+esc(b[1])+'</span></div>';
  });
  return '<div class="panel-card tab-panel" id="panel-blocks">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[2].icon+'</span>用到的 mBlock 积木</h3>' +
    '<div class="blk-list">'+rows+'</div>' +
    '<div class="tip-box">在 mBlock 5 中选择「CyberPi」设备，从对应分类里拖出这些积木，像拼乐高一样把它们接起来。</div></div>';
}

/* ---- 面板：CyberPi 演示 ---- */
function panelDemo(l, ch){
  return '<div class="panel-card tab-panel" id="panel-demo">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[3].icon+'</span>CyberPi 演示项目</h3>' +
    '<div class="proj-card"><div class="p-name"><span class="t-ico" style="background:hsl(0 0% 100% / .22)">'+TABS[3].icon+'</span>'+esc(l.projName)+'</div>' +
    '<div class="p-eff">'+esc(l.projEff)+'</div></div>' +
    '<div class="steps-list">' + l.steps.map(function(s, i){
      return '<div class="step-item"><span class="s-no">'+(i+1)+'</span><p>'+esc(s)+'</p></div>';
    }).join('') + '</div>' +
    '<div class="hw-chips">'+ l.hardware.map(function(h){ return '<span class="hw-chip">'+esc(h)+'</span>'; }).join('') + '</div></div>';
}

/* ---- 面板：动手挑战 ---- */
function panelChallenge(l, ch){
  return '<div class="panel-card tab-panel" id="panel-challenge">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[4].icon+'</span>动手挑战</h3>' +
    '<div class="challenge-box"><span class="c-tag">小创客任务</span><p>'+esc(l.challenge)+'</p></div>' +
    (l.tip ? '<div class="tip-box"><b>老师小贴士：</b>'+esc(l.tip)+'</div>' : '') + '</div>';
}

/* ---- 面板：知识问答 ---- */
function panelQuiz(l, ch){
  return '<div class="panel-card tab-panel" id="panel-quiz">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[5].icon+'</span>随堂问答</h3>' +
    '<div class="quiz-wrap"><div class="quiz-head">' +
    '<span class="q-prog" id="quizProg">第 1 / '+l.quiz.length+' 题</span>' +
    '<span class="chip light" id="quizScore">答对 0 题 · 答错 0 次</span></div>' +
    '<div class="q-card" id="quizCard"></div></div></div>';
}
function renderQuiz(){
  var l = COURSE[quizState.id];
  var q = l.quiz[quizState.idx];
  var opts = ['A','B','C','D'];
  var html = '<div class="q-text">'+esc(q.q)+'</div><div class="q-opts">';
  q.o.forEach(function(o, i){
    html += '<button class="q-opt" data-i="'+i+'" onclick="answerQuiz(this)"><span class="q-letter">'+opts[i]+'</span><span>'+esc(o)+'</span></button>';
  });
  html += '</div><div class="q-explain" id="qExplain"></div><button class="btn q-next" id="qNext" onclick="nextQuiz()">下一题</button>';
  document.getElementById('quizCard').innerHTML = html;
  document.getElementById('quizProg').textContent = '第 ' + (quizState.idx+1) + ' / ' + l.quiz.length + ' 题';
  document.getElementById('quizScore').textContent = '答对 ' + quizState.correct + ' 题 · 答错 ' + quizState.wrong + ' 次';
}
function answerQuiz(btn){
  var l = COURSE[quizState.id];
  var q = l.quiz[quizState.idx];
  var i = parseInt(btn.getAttribute('data-i'), 10);
  var options = document.querySelectorAll('#quizCard .q-opt');
  if(btn.disabled) return;
  if(i === q.a){
    btn.classList.add('correct');
    options.forEach(function(o){ o.disabled = true; });
    if(!btn.classList.contains('wrong')) quizState.firstTry++;
    quizState.correct++;
    var ex = document.getElementById('qExplain');
    ex.style.display = 'block';
    ex.style.background = 'hsl(150 60% 95%)';
    ex.style.borderColor = 'hsl(150 60% 60%)';
    ex.innerHTML = '<b style="color:var(--ok)">答对啦！</b> ' + esc(q.exp);
    var nb = document.getElementById('qNext');
    nb.style.display = 'inline-flex';
    nb.textContent = (quizState.idx === l.quiz.length - 1) ? '查看本课成绩' : '下一题';
  } else {
    btn.classList.add('wrong');
    btn.disabled = true;
    quizState.wrong++;
    var ex2 = document.getElementById('qExplain');
    ex2.style.display = 'block';
    ex2.style.background = 'hsl(0 72% 96%)';
    ex2.style.borderColor = 'hsl(0 72% 75%)';
    ex2.innerHTML = '<b style="color:var(--bad)">答错啦，再想想！</b> 正确答案就在剩下的选项里，答对后我会给你讲解。';
    document.getElementById('quizScore').textContent = '答对 ' + quizState.correct + ' 题 · 答错 ' + quizState.wrong + ' 次';
  }
}
function nextQuiz(){
  var l = COURSE[quizState.id];
  if(quizState.idx < l.quiz.length - 1){
    quizState.idx++;
    renderQuiz();
  } else {
    finishQuiz();
  }
}
function finishQuiz(){
  var l = COURSE[quizState.id];
  var time = Math.round((Date.now() - quizState.start) / 1000);
  var d = DB.get();
  var rec = DB.lessonRec(d, quizState.id);
  rec.done = true;
  rec.correct = quizState.firstTry;
  rec.wrong = quizState.wrong;
  rec.time = time;
  d.records[quizState.id] = rec;
  DB.save(d);
  quizState.done = true;

  var done = DB.doneCount(d);
  var msg = done === 32 ? '太厉害了！32 课全部完成，你是毕业工程师！' : '本课完成！继续下一站探险吧。';
  var nextId = quizState.id < 32 ? quizState.id + 1 : quizState.id;
  document.getElementById('quizCard').innerHTML =
    '<div class="quiz-done">' +
    '<div class="big-emoji" style="font-size:52px;line-height:1">★</div>' +
    '<h3>本课完成！</h3><p>'+msg+'</p>' +
    '<div class="quiz-stats">' +
      '<span class="qs-pill ok">✓ 首次答对 '+quizState.firstTry+' 题</span>' +
      '<span class="qs-pill bad">✗ 答错 '+quizState.wrong+' 次</span>' +
      '<span class="qs-pill time">用时 '+time+' 秒</span>' +
    '</div>' +
    '<button class="btn" style="margin-top:20px" onclick="go(\'#/course/'+nextId+'\')">' +
      (quizState.id < 32 ? '去下一课 →' : '回到首页') + '</button></div>';
  document.getElementById('quizProg').textContent = '已完成';
  document.getElementById('quizScore').textContent = '答对 ' + quizState.correct + ' 题 · 答错 ' + quizState.wrong + ' 次';
  document.getElementById('ctRing').style.setProperty('--p', 100);
  document.getElementById('ctRingPct').textContent = '✓';
  document.getElementById('ctProgTxt').textContent = '本课已完成';
  if(location.hash === '#/home'){ renderHome(); }
  if(location.hash === '#/growth'){ renderGrowth(); }
}

/* ============ 硬件页 ============ */
var HW_PARTS = [
  {key:'display', name:'1.44 英寸全彩屏', desc:'128×128 个像素小格子。显示文字、数字、图片，还能画像素画——第 5、6、7 课的主角。'},
  {key:'joystick', name:'五向摇杆', desc:'可以上下左右拨动、还可以按下确认。它是 CyberPi 的“方向盘”，第 6 课调颜色用它。'},
  {key:'btnA', name:'按钮 A', desc:'像游戏手柄的按键。程序里可以用“当按钮A被按下时”触发事情，是常用的“输入”。'},
  {key:'btnB', name:'按钮 B', desc:'和按钮 A 配合使用：一个负责“上一步”，一个负责“确认”。第 4 课计数器就用它清零。'},
  {key:'home', name:'HOME 键', desc:'回到系统主界面，相当于手机的“主页键”。长按可以进入系统设置。'},
  {key:'mic', name:'麦克风', desc:'收集声音信息：既能当“声音传感器”（第 13 课分拣声音），也能做语音识别——AI 的“耳朵”。'},
  {key:'light', name:'光线传感器', desc:'测量环境光的亮暗，数值会在 0–100 之间变化。第 8 课的数据过滤就是靠它。'},
  {key:'speaker', name:'扬声器', desc:'播放声音和音乐，还能用“朗读”积木把文字变成声音——AI 的“嘴巴”（语音合成）。'},
  {key:'rgb', name:'RGB 灯 ×5', desc:'5 颗可以编程的彩色灯，红绿蓝三种光混合出任何颜色。第 2 课的 0 和 1、第 6 课的调色都靠它。'},
  {key:'gyro', name:'6 轴陀螺仪 + 加速度计', desc:'感知倾斜、摇晃和移动。第 14 课“摇一摇识方向”、第 31 课“合作救援”都用它。'},
  {key:'wifi', name:'Wi-Fi + 蓝牙', desc:'连接网络后，CyberPi 可以上网：语音识别、获取天气、设备互联（第 19、25、26 课需要）。'},
  {key:'typec', name:'Type-C 接口', desc:'连接电脑上传程序、给设备供电充电。是编程和 CyberPi 之间的“桥梁”。'},
  {key:'mbuild', name:'扩展接口', desc:'连接更多电子模块：温湿度传感器、AI 摄像头、舵机等，让 CyberPi 的本领越来越大。'}
];
function renderHardware(){
  var W = 480, H = 270;
  var svg = '<svg viewBox="0 0 '+W+' '+H+'" style="width:100%;height:auto" role="img" aria-label="CyberPi 硬件图解">';
  svg += '<defs><linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F2F8FF"/><stop offset="1" stop-color="#DCEBFB"/></linearGradient></defs>';
  svg += '<rect x="14" y="14" width="452" height="242" rx="28" fill="url(#bd)" stroke="#A9C9EC" stroke-width="2"/>';
  svg += '<rect x="24" y="24" width="432" height="222" rx="20" fill="none" stroke="#C8DFF4" stroke-width="1.2" stroke-dasharray="5 5"/>';
  svg += '<text x="38" y="44" font-size="12" font-weight="800" fill="#5D82A8" letter-spacing="1">CyberPi · 童芯派</text>';

  svg += '<g class="hotspot" data-hw="display" onclick="hwInfo(\'display\')"><rect x="150" y="52" width="180" height="112" rx="10" fill="#12294A" stroke="#0A1B30" stroke-width="2"/>' +
    '<circle cx="196" cy="96" r="7" fill="#FFD166"/><circle cx="250" cy="96" r="7" fill="#FFD166"/>' +
    '<path d="M196 130 q28 26 54 0" stroke="#7EE0A3" stroke-width="6" fill="none" stroke-linecap="round"/>' +
    '<text x="240" y="40" text-anchor="middle" font-size="11" font-weight="800" fill="#2E5B92">显示屏</text></g>';

  svg += '<g class="hotspot" data-hw="joystick" onclick="hwInfo(\'joystick\')"><circle cx="70" cy="88" r="19" fill="#fff" stroke="#7FA8D8" stroke-width="2.5"/>' +
    '<circle cx="70" cy="88" r="9" fill="#BBD8F5"/><path d="M70 66v44M48 88h44" stroke="#9DC2E8" stroke-width="3" stroke-linecap="round"/>' +
    '<text x="70" y="132" text-anchor="middle" font-size="11" font-weight="800" fill="#2E5B92">五向摇杆</text></g>';

  svg += '<g class="hotspot" data-hw="btnA" onclick="hwInfo(\'btnA\')"><circle cx="368" cy="84" r="14" fill="#FF7A7A" stroke="#E05757" stroke-width="2"/>' +
    '<text x="368" y="89" text-anchor="middle" font-size="13" font-weight="800" fill="#fff">A</text>' +
    '<text x="368" y="120" text-anchor="middle" font-size="11" font-weight="800" fill="#2E5B92">按钮 A</text></g>';
  svg += '<g class="hotspot" data-hw="btnB" onclick="hwInfo(\'btnB\')"><circle cx="368" cy="138" r="14" fill="#4C97FF" stroke="#2E6FD8" stroke-width="2"/>' +
    '<text x="368" y="143" text-anchor="middle" font-size="13" font-weight="800" fill="#fff">B</text>' +
    '<text x="368" y="174" text-anchor="middle" font-size="11" font-weight="800" fill="#2E5B92">按钮 B</text></g>';

  svg += '<g class="hotspot" data-hw="home" onclick="hwInfo(\'home\')"><rect x="352" y="190" width="34" height="12" rx="5" fill="#9AA7B8"/>' +
    '<text x="369" y="199" text-anchor="middle" font-size="8" font-weight="800" fill="#fff">HOME</text>' +
    '<text x="369" y="222" text-anchor="middle" font-size="10" font-weight="800" fill="#2E5B92">HOME 键</text></g>';

  svg += '<g class="hotspot" data-hw="mic" onclick="hwInfo(\'mic\')"><circle cx="112" cy="138" r="11" fill="#6BCB77" stroke="#4DA85A" stroke-width="2"/>' +
    '<circle cx="112" cy="138" r="4" fill="#fff"/>' +
    '<text x="112" y="170" text-anchor="middle" font-size="11" font-weight="800" fill="#2E5B92">麦克风</text></g>';

  svg += '<g class="hotspot" data-hw="light" onclick="hwInfo(\'light\')"><circle cx="66" cy="170" r="11" fill="#FFD166" stroke="#E0AC2E" stroke-width="2"/>' +
    '<path d="M66 150v-6M50 158l-4-4M82 158l4-4" stroke="#FFD166" stroke-width="2.4" stroke-linecap="round"/>' +
    '<text x="66" y="202" text-anchor="middle" font-size="10.5" font-weight="800" fill="#2E5B92">光线传感器</text></g>';

  svg += '<g class="hotspot" data-hw="speaker" onclick="hwInfo(\'speaker\')"><rect x="52" y="216" width="78" height="20" rx="6" fill="#DCE7F5" stroke="#A9C0DC" stroke-width="1.5"/>' +
    '<path d="M66 220v12M78 220v12M90 220v12M104 220v12" stroke="#A9C0DC" stroke-width="1.6"/>' +
    '<text x="52" y="252" font-size="11" font-weight="800" fill="#2E5B92">扬声器</text></g>';

  var rgbCols = ['#FF5F5F','#5FC95F','#5F8BFF','#FF5F5F','#5FC95F'];
  var rgbG = '<g class="hotspot" data-hw="rgb" onclick="hwInfo(\'rgb\')">';
  var i;
  for(i=0;i<5;i++){ rgbG += '<circle cx="'+(192+i*22)+'" cy="212" r="7.5" fill="'+rgbCols[i]+'" stroke="#fff" stroke-width="2"/>'; }
  rgbG += '<text x="240" y="238" text-anchor="middle" font-size="10.5" font-weight="800" fill="#2E5B92">RGB 灯 ×5</text></g>';
  svg += rgbG;

  svg += '<g class="hotspot" data-hw="gyro" onclick="hwInfo(\'gyro\')"><rect x="300" y="206" width="58" height="20" rx="5" fill="#C9D8EC" stroke="#9DB4D6" stroke-width="1.5"/>' +
    '<circle cx="316" cy="216" r="4" fill="#7FA8D8"/><circle cx="330" cy="216" r="4" fill="#7FA8D8"/>' +
    '<text x="329" y="244" text-anchor="middle" font-size="10" font-weight="800" fill="#2E5B92">陀螺仪+加速度计</text></g>';

  svg += '<g class="hotspot" data-hw="wifi" onclick="hwInfo(\'wifi\')"><rect x="248" y="34" width="76" height="20" rx="5" fill="#B9D6F2" stroke="#8FB6DE" stroke-width="1.5"/>' +
    '<path d="M272 44a8 8 0 0 1 12 0M276 48a4 4 0 0 1 4 0" stroke="#2E6FD8" stroke-width="1.8" fill="none" stroke-linecap="round"/>' +
    '<text x="286" y="72" text-anchor="middle" font-size="10.5" font-weight="800" fill="#2E5B92">Wi-Fi + 蓝牙</text></g>';

  svg += '<g class="hotspot" data-hw="typec" onclick="hwInfo(\'typec\')"><rect x="416" y="216" width="32" height="14" rx="4" fill="#7FA8D8"/>' +
    '<path d="M424 220h16M424 224h16" stroke="#fff" stroke-width="1.4"/>' +
    '<text x="432" y="252" text-anchor="middle" font-size="10" font-weight="800" fill="#2E5B92">Type-C</text></g>';

  svg += '<g class="hotspot" data-hw="mbuild" onclick="hwInfo(\'mbuild\')"><rect x="410" y="100" width="34" height="36" rx="7" fill="#E5C7F7" stroke="#B78AD6" stroke-width="1.5"/>' +
    '<circle cx="427" cy="112" r="3" fill="#B78AD6"/><circle cx="427" cy="124" r="3" fill="#B78AD6"/>' +
    '<text x="427" y="156" text-anchor="middle" font-size="10" font-weight="800" fill="#2E5B92">扩展接口</text></g>';

  svg += '</svg>';
  document.getElementById('hwSvgCard').innerHTML = svg;
  hwInfo('display');
}
function hwInfo(key){
  var p = null;
  HW_PARTS.forEach(function(x){ if(x.key === key) p = x; });
  if(!p) return;
  document.getElementById('hwInfo').innerHTML =
    '<div class="hi-name"><span style="display:inline-grid;place-items:center;width:26px;height:26px;border-radius:8px;background:var(--primary);color:#fff">●</span>'+p.name+'</div>' +
    '<div class="hi-desc">'+p.desc+'</div>';
}

/* ============ 成长页 ============ */
var BADGES = [
  {id:'start', name:'初来乍到', desc:'完成第 1 节课', icon:'★', need:function(d){ return DB.doneCount(d) >= 1; }},
  {id:'ch1', name:'信息小侦探', desc:'完成第一章 8 课', icon:'◎', need:function(d){ return chDone(d,1) >= 8; }},
  {id:'ch2', name:'算法小达人', desc:'完成第二章 8 课', icon:'◇', need:function(d){ return chDone(d,2) >= 8; }},
  {id:'ch3', name:'机器学习家', desc:'完成第三章 8 课', icon:'△', need:function(d){ return chDone(d,3) >= 8; }},
  {id:'ch4', name:'AI 安全卫士', desc:'完成第四章 8 课', icon:'○', need:function(d){ return chDone(d,4) >= 8; }},
  {id:'grad', name:'毕业工程师', desc:'完成全部 32 课', icon:'♛', need:function(d){ return DB.doneCount(d) >= 32; }}
];
function chDone(d, ch){
  return ALL.filter(function(l){ return l.ch === ch && (d.records[l.id]||{}).done; }).length;
}
function renderGrowth(){
  var d = DB.get();
  var done = DB.doneCount(d);
  var pct = Math.round(done / 32 * 100);
  var correct = 0;
  Object.keys(d.records).forEach(function(k){ correct += d.records[k].correct; });
  var earned = BADGES.filter(function(b){ return b.need(d); }).length;

  document.getElementById('growRing').style.setProperty('--p', pct);
  document.getElementById('growPct').textContent = pct + '%';
  document.getElementById('growName').textContent = (d.nick || '小探险家') + (done === 32 ? '，毕业快乐！' : (done > 0 ? '，继续加油！' : '，准备好出发了吗？'));
  document.getElementById('gsDone').textContent = done;
  document.getElementById('gsQuiz').textContent = correct;
  document.getElementById('gsBadge').textContent = earned;

  document.getElementById('badgeGrid').innerHTML = BADGES.map(function(b){
    var ok = b.need(d);
    return '<div class="badge'+(ok?' earned':'')+'"><div class="b-ico">'+b.icon+'</div><b>'+b.name+'</b><p>'+b.desc+'</p></div>';
  }).join('');

  document.getElementById('growCh').innerHTML = CHAPTERS.map(function(ch){
    var c = chDone(d, ch.id);
    return '<div class="grow-ch-row"><span class="gcr-ico" style="background:'+ch.color+'">'+ch.id+'</span><b>'+ch.name+'</b>' +
      '<div class="gcr-bar"><i style="width:'+(c/8*100)+'%"></i></div><span class="gcr-num">'+c+' / 8</span></div>';
  }).join('');

  var recs = ALL.filter(function(l){ return (d.records[l.id]||{}).done; });
  if(recs.length === 0){
    document.getElementById('growRecords').innerHTML = '<div style="background:#fff;border-radius:14px;padding:26px;text-align:center;color:var(--ink-2);font-weight:600">还没有学习记录，去完成第一课吧！</div>';
  } else {
    document.getElementById('growRecords').innerHTML = recs.map(function(l){
      var r = d.records[l.id];
      return '<div class="grow-ch-row"><span class="gcr-ico" style="background:'+chColor(l.ch)+'">'+l.id+'</span><b>'+esc(l.title)+'</b>' +
        '<span style="font-size:12.5px;color:var(--ink-2);font-weight:700">首次答对 '+r.correct+' 题</span>' +
        '<span class="gcr-num" style="color:var(--ok)">已完成 ✓</span></div>';
    }).join('');
  }
}
function resetAll(){
  if(confirm('确定要清空所有学习记录吗？')){
    localStorage.removeItem('cyberpi_course');
    location.hash = '#/home';
    location.reload();
  }
}

/* ============ 初始化 ============ */
window.addEventListener('hashchange', route);
window.addEventListener('DOMContentLoaded', function(){
  renderNick();
  route();
});
document.addEventListener('keydown', function(e){
  if(e.key === 'Enter' && document.getElementById('nickOverlay').style.display === 'grid'){ saveNick(); }
});
