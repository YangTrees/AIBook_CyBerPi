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
ALL.forEach(function(l){
  var refinement = CURRICULUM_REFINEMENTS[l.id];
  if(refinement){
    l.programMeaning = refinement.meaning;
    l.programObserve = refinement.observe;
    l.programHook = refinement.hook;
    l.programGoal = refinement.goal;
    l.programWatch = refinement.watch;
    l.transfer = refinement.transfer;
  }
  COURSE[l.id] = l;
});

/* 积木分类颜色 */
var CAT_COLOR = {事件:'var(--cat-event)',控制:'var(--cat-control)',显示:'var(--cat-display)',灯:'var(--cat-light)',声音:'var(--cat-sound)',传感:'var(--cat-sense)',运算:'var(--cat-op)',变量:'var(--cat-var)','网络/AI':'var(--cat-ai)',扩展:'var(--cat-ext)',自制:'var(--cat-my)',侦测:'var(--cat-sense)',外观:'var(--cat-display)',循环:'var(--cat-control)',列表:'var(--cat-var)',随机:'var(--cat-op)'};

/* 同类积木扩展：用于课程页的可展开积木百科 */
var BLOCK_FAMILIES = {
  '事件':['当程序开始运行','当按键被按下','当摇杆向指定方向','当收到广播消息','广播消息'],
  '控制':['等待若干秒','重复执行若干次','一直重复执行','如果…那么','如果…那么…否则','重复执行直到','停止程序'],
  '显示':['显示文字','显示数字','设置文字大小与颜色','清空屏幕','绘制点、线与图形','设置显示位置'],
  '灯':['点亮全部RGB灯','熄灭全部RGB灯','设置RGB颜色','设置第N颗灯','设置灯光亮度','播放灯光动画'],
  '声音':['播放音符','播放内置音效','设置音量','录制声音','播放录音','停止所有声音'],
  '传感':['按钮是否按下','摇杆方向与坐标','环境光强度','声音强度','加速度','倾斜角度','摇一摇状态'],
  '侦测':['询问并等待','读取回答','按键是否按下','鼠标位置','碰到指定对象','计时器'],
  '外观':['说出文字','切换造型','改变大小','显示或隐藏角色','切换背景','添加图形效果'],
  '运算':['加减乘除','比较大小','且 / 或 / 不成立','生成随机数','连接文字','判断文字是否包含'],
  '随机':['生成范围内随机数','按权重抽取结果','随机打乱列表'],
  '变量':['建立变量','变量设为指定值','变量增加或减少','显示变量','隐藏变量'],
  '列表':['新建列表','加入一项','读取第N项','替换列表项','删除列表项','获取列表长度'],
  '扩展':['图像分类','姿态或声音识别','训练并使用模型','读取模型结果','置信度判断'],
  '网络/AI':['连接网络服务','语音识别','语音合成','读取识别结果','发送或接收数据'],
  '自制':['定义自制积木','添加输入参数','运行自制积木','设置不刷新屏幕运行']
};

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
function lessonAsset(id){
  return 'assets/prototype/lesson-' + (id < 10 ? '0' + id : '' + id) + '-v3-web.jpg';
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
        '<div class="lc-cover"><img src="'+lessonAsset(l.id)+'" alt="'+esc(l.title)+'">' +
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
  {key:'intro', name:'故事回声', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'},
  {key:'know', name:'学习目标', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 19.5a5.5 5.5 0 0 1-5.5-5.5V5h16v9a5.5 5.5 0 0 1-5.5 5.5h-5z"/><path d="M12 5v10"/></svg>'},
  {key:'blocks', name:'积木程序', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="12" height="10" rx="2.5"/><rect x="16.5" y="7" width="4.5" height="10" rx="2"/><path d="M9 7V5"/></svg>'},
  {key:'demo', name:'编程任务', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="12" rx="3"/><circle cx="12" cy="12" r="3.2"/><path d="M7 6V4h10v2"/></svg>'},
  {key:'challenge', name:'试玩与升级', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 13.5H11L9.5 22 19 10h-6.5L13 2z"/></svg>'},
  {key:'quiz', name:'挑战与问答', icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.4 2.3c-.8.3-.9 1-.9 1.7M12 17h.01"/></svg>'}
];
var TASK_LEVEL_ICONS = [
  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3v18"/><path d="M5 5h11l-2.5 3L16 11H5"/><path d="m8.5 16.5 2 2 4-4"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 2.7 5.5 6.1.9-4.4 4.3 1 6.1-5.4-2.9-5.4 2.9 1-6.1-4.4-4.3 6.1-.9L12 3z"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 22h4"/><path d="M8.4 14.5A6 6 0 1 1 15.6 14.5C14.6 15.2 14 16 14 17h-4c0-1-.6-1.8-1.6-2.5z"/><path d="M12 6v3M8.8 8.2l2.1 2.1M15.2 8.2l-2.1 2.1"/></svg>'
];
var SAMPLE_CONTENT = {
  1:{
    driving:"按下 CyberPi 的真实按钮后，输入怎样经过程序处理，变成屏幕和灯光的回应？",
    deliverable:"在 mBlock 上传模式完成“线索接收器”：开机显示侦探身份；每按一次 A，线索计数增加，并根据数量显示不同回应、亮起绿色 RGB 灯。",
    prep:["打开 mBlock，在设备区添加“童芯派”","使用 Type-C 数据线连接，确认界面显示“设备已连接”","切换上传模式，准备建立“线索计数”变量并烧录到设备"],
    stepTitles:["连接设备并选上传模式","加入开机身份提示","按钮 A 让线索计数加一","按数量显示不同回应","上传后按实体 A 键验证"],
    phases:["设备连接","输入事件","输出搭建","参数调试","真机验证"],
    levels:[["必做任务","连续按两次实体按钮 A，屏幕先显示“收到1条线索”，再显示“线索够啦！”，同时亮绿灯。"],["加星任务","增加按钮 B 清零程序，屏幕显示“线索已清空”。"],["创造任务","为第3、第4条线索设计新的文字、颜色或声音反馈。"]],
    tests:[["上传后重新启动","屏幕显示“我是线索小侦探”","初始化"],["第一次按实体按钮 A","计数为1，显示“收到1条线索”","输入与变量"],["第二次按实体按钮 A","计数为2，显示“线索够啦！”","条件分支"],["继续按 A","计数持续增加且绿灯反馈正常","连续运行"],["修改判断阈值后重新上传","回应切换时机随阈值改变","修改—上传—验证"]],
    bugs:[["按 A 完全没有反应","检查是否选中童芯派、是否已上传成功，以及事件积木下拉项是否为 A。"],["每次都显示同一句话","检查线索计数是否在按钮事件中增加，以及 if 条件是否读取了正确变量。"],["重新开机仍保留旧效果","停止当前程序，重新上传；上传完成后重启 CyberPi 再测试。"]],
    reflection:["在这套程序里，哪一部分是输入、处理和输出？","mBlock 与 CyberPi 各自负责什么，缺少其中一个还能完成本课验证吗？"],
    success:["程序已上传并可脱离电脑运行","连续按 A 后计数与文字分支正确变化","能够指出按钮是输入、变量和条件是处理、屏幕与灯光是输出"]
  },
  17:{
    driving:"怎样证明模型学会了规律，而不是只记住训练时见过的图片？",
    deliverable:"训练圆形与三角形分类器，用完全没有参与训练的新卡片考试，记录准确率和错误样本，并在 CyberPi 上显示测试结论。",
    prep:["把图形卡分成训练袋和测试袋，测试袋先封存","保证两类训练样本数量接近，并包含不同角度和光线","建立测试总数、正确数和准确率记录表"],
    stepTitles:["分开训练与测试","采集两类样本","训练分类模型","新卡片考试","补充样本复测"],
    levels:[["必做任务","使用独立测试卡完成至少10次测试并计算准确率。"],["加星任务","比较每类5张与每类15张训练图的测试结果。"],["创造任务","增加第三个类别，重新设计训练和测试方案。"]],
    tests:[["训练图再次识别","通常较容易正确","不能作为考试成绩"],["全新圆形卡","判断为圆形","泛化能力"],["旋转后的三角形","判断为三角形","角度变化"],["光线较暗的新卡","记录判断与置信表现","环境变化"]],
    bugs:[["测试准确率异常高","检查测试图片是否曾混入训练集，避免“题目泄露”。"],["换角度就识别错误","训练样本可能过于单一，需要补充角度、大小和光线变化。"]],
    reflection:["为什么训练集成绩高，不代表模型面对新图片也可靠？","补充什么样的样本，比简单复制同一张图片更有用？"]
  },
  30:{
    driving:"一次结果不同就是不公平吗？怎样用重复实验找到真正的规则偏差？",
    deliverable:"制作100轮公平检测器，对比50/50与70/30两种抽签规则，用多组数据说明差异来自随机波动还是规则偏斜。",
    prep:["建立甲组次数、乙组次数和实验轮数变量","准备50/50与70/30两套分界规则","设计每组实验的结果记录表"],
    stepTitles:["变量清零","运行公平规则","记录多组结果","制造偏斜规则","比较并提出修改"],
    levels:[["必做任务","完成一组50/50规则下的100轮实验并保存结果。"],["加星任务","两种规则各运行5组，比较平均差值。"],["创造任务","设计一种新的抽样规则，并说明它为什么更公平或更不公平。"]],
    tests:[["50/50运行100轮","两组次数接近但不必完全相同","随机波动"],["50/50重复5组","差异方向不固定","多次证据"],["70/30重复5组","甲组持续明显更高","规则偏斜"],["恢复50/50复测","稳定差异减小","修改验证"]],
    bugs:[["每组结果越来越大","新一组实验前没有把计数变量清零。"],["50/50实际不是一半机会","检查随机数范围和分界值是否包含或遗漏边界。"]],
    reflection:["什么证据能让你更有把握地说规则存在偏差？","结果次数之外，还需要检查哪些输入、规则和影响？"]
  }
};
var quizState = null;
var imageZoom = 1;
var imageFitWidth = 0;

function sampleOf(l){ return SAMPLE_CONTENT[l.id] || null; }
function taskSpec(l){
  if(l.transfer){
    return {
      driving:'学会“'+l.projName+'”以后，怎样保留核心逻辑，把它改造成“'+l.transfer.name+'”？',
      deliverable:l.transfer.eff,
      prep:['先完成并解释前一模块的“'+l.projName+'”示范程序','复制原工程并另存为新名称，不在原程序上直接覆盖','圈出需要保留、替换和新增的积木，先画出改造路线'],
      levels:[['必做任务','按5个迁移步骤完成“'+l.transfer.name+'”，并通过基础测试。'],['加星任务',l.transfer.challenge],['创造任务','再更换一种输入、规则或反馈，说明它与示范程序的相同点和不同点。']],
      tests:[['运行原示范程序','能说出原程序的输入、处理和输出','先理解再改造'],['运行迁移任务基础情境','新作品按规则产生正确反馈','核心逻辑迁移'],['测试边界或相反情境','不同条件进入不同分支','规则完整性'],['修改一个参数后复测','现象随修改产生可解释变化','改进与证据']],
      bugs:[['改完后仍像原作品','检查是否真正替换了输入情境、处理规则或输出目标，而不只是改文字。'],['新功能互相覆盖','逐个关闭新增模块分段测试，确认变量、事件和屏幕输出不会冲突。'],['结果偶尔不稳定','记录触发时的真实传感数值，检查阈值、等待时间和边界条件。']],
      reflection:['示范程序中哪一条核心逻辑被保留下来？迁移任务改变了什么？','如果把新任务交给另一位同学，他能根据说明独立完成和验证吗？']
    };
  }
  var s = sampleOf(l);
  if(s) return s;
  return {
    driving:'怎样在 mBlock 中把“'+l.theme+'”变成一个可以在 CyberPi 上运行和验证的作品？',
    deliverable:'完成“'+l.projName+'”：按步骤搭建积木、上传到 CyberPi，并用实体按钮或传感器验证“输入—处理—输出”是否符合预期。',
    prep:['用 Type-C 数据线连接 CyberPi，在 mBlock 设备区确认已识别童芯派','根据本课功能选择在线模式调试或上传模式独立运行','先读一遍完整程序与 5 个步骤，找出输入、处理和输出积木'],
    levels:[['必做任务','完成核心程序并在 CyberPi 真机上通过基础测试。'],['加星任务',l.challenge],['创造任务','更换一种输入或输出方式，说明改动后程序逻辑有什么变化。']],
    tests:[['设备连接并启动','CyberPi 显示本课启动提示','连接与初始化'],['触发本课输入','程序进入正确的处理分支','事件与传感输入'],['观察真机输出','屏幕、灯光或声音与任务说明一致','硬件反馈'],['修改一个参数后重测','结果随参数发生可解释的变化','修改与验证']],
    bugs:[['程序没有反应','确认设备已连接、运行模式正确，并检查事件积木是否接在程序最上方。'],['输出与预期不同','逐段运行，核对条件、变量初值和显示、灯光或声音参数。'],['上传后仍是旧效果','停止当前程序，重新上传；完成后重启 CyberPi 再验证。']],
    reflection:['本课程序的真实输入、逻辑处理和硬件输出分别是什么？','这个作品是在模拟 AI 概念，还是实际调用了 AI 模型？你能说出证据吗？']
  };
}
function conciseStepTitle(step, i){
  var text = String(step).replace(/^（[^）]+）/,'').replace(/^\([^\)]+\)/,'');
  return text || ('关键步骤 '+(i+1));
}
function openImgLightbox(src, label){
  var box = document.getElementById('imgLightbox');
  var img = document.getElementById('lightboxImg');
  imageZoom = 1;
  imageFitWidth = 0;
  img.alt = label || '积木程序截图放大查看';
  document.getElementById('lightboxCaption').textContent = label || '积木程序截图放大查看';
  img.style.width = '';
  document.getElementById('zoomValue').textContent = '100%';
  box.style.display = 'flex';
  document.body.classList.add('lightbox-open');
  function fitImage(){
    var stage = document.querySelector('.lightbox-stage');
    var fit = Math.min((stage.clientWidth-40)/img.naturalWidth, (stage.clientHeight-40)/img.naturalHeight, 1);
    imageFitWidth = Math.max(1, Math.round(img.naturalWidth*fit));
    img.style.width = imageFitWidth+'px';
  }
  img.onload = fitImage;
  img.src = src;
  if(img.complete && img.naturalWidth) fitImage();
}
function closeImgLightbox(){
  document.getElementById('imgLightbox').style.display = 'none';
  document.body.classList.remove('lightbox-open');
}
function setImageZoom(next){
  imageZoom = Math.max(.5, Math.min(3, next));
  var img = document.getElementById('lightboxImg');
  if(imageFitWidth) img.style.width = Math.round(imageFitWidth*imageZoom)+'px';
  document.getElementById('zoomValue').textContent = Math.round(imageZoom*100)+'%';
}
function changeImageZoom(delta){ setImageZoom(imageZoom + delta); }
function resetImageZoom(){ setImageZoom(1); }
function sampleDriving(l){
  var question = '“'+l.theme+'”怎样通过“'+l.projName+'”变成可以观察、运行和解释的程序？';
  return '<div class="sample-driving"><span>本课驱动问题</span><b>'+esc(question)+'</b><p>先说出你的猜想，完成示范程序后再回来修正答案。</p></div>';
}
function sampleMediaStudio(l){
  var pad = l.id < 10 ? '0'+l.id : ''+l.id;
  var codeImage = 'assets/blocks/lesson-'+pad+'/full-program.png';
  var codeAlt = '第'+l.id+'课 mBlock 积木搭建示意';
  var stepTitles = l.steps.map(conciseStepTitle);
  return '<section class="media-studio"><div class="media-studio-head"><div><span>COURSE MEDIA · 素材区</span><h4>mBlock 积木搭建示意与 CyberPi 效果</h4></div><p>当前图片用于讲解搭建思路，后续可替换为真实操作截图；点击可放大到 300%。</p></div>'+
    '<div class="media-featured"><div class="video-slot" style="--poster:url(\''+lessonAsset(l.id)+'\')"><div class="play-mark">▶</div><b>最终效果视频</b><span>程序运行 + CyberPi 反馈 · 30–90 秒</span><em>待上传</em></div>'+
    '<figure class="full-code-slot zoomable-shot" onclick="openImgLightbox(\''+codeImage+'\',\''+esc(codeAlt)+'\')"><img src="'+codeImage+'" alt="'+codeAlt+'"><span class="zoom-badge">点击放大</span><figcaption><b>积木搭建示意图</b><span>根据本课步骤生成 · 点击查看细节</span><em>可替换实拍</em></figcaption></figure></div>'+
    '<div class="step-shot-head"><b>关键步骤截图</b><span>第 2–4 步已配图，点击可放大</span></div><div class="step-shot-grid">'+stepTitles.map(function(n,i){
      var shot = (i >= 1 && i <= 3) ? 'assets/blocks/lesson-'+pad+'/step-0'+(i+1)+'.png' : '';
      return shot ? '<div class="shot-slot has-shot zoomable-shot" onclick="openImgLightbox(\''+shot+'\',\''+esc(n)+'\')"><span>0'+(i+1)+'</span><img src="'+shot+'" alt="'+esc(n)+'"><b>'+esc(n)+'</b><small>点击图片放大查看</small></div>' : '<div class="shot-slot"><span>0'+(i+1)+'</span><i>'+((i===0)?'准备':'验证')+'</i><b>'+esc(n)+'</b><small>'+((i===0)?'先完成设备与变量准备':'在 CyberPi 真机完成验收')+'</small></div>';
    }).join('')+'</div></section>';
}
function sampleTaskLab(l){
  var s = taskSpec(l);
  return '<section class="sample-task-lab"><div class="sample-brief"><span>今天要做出</span><b>'+esc(s.deliverable)+'</b></div><div class="sample-task-grid"><div class="prep-card"><span>出发前准备</span><ol>'+s.prep.map(function(n){return '<li>'+esc(n)+'</li>';}).join('')+'</ol></div><div class="level-card"><span>选择你的挑战</span>'+s.levels.map(function(n,i){return '<article class="level-'+i+'"><i aria-hidden="true">'+TASK_LEVEL_ICONS[i]+'</i><div><b>'+esc(n[0])+'</b><p>'+esc(n[1])+'</p></div></article>';}).join('')+'</div></div></section>';
}
function platformWorkflow(l){
  var seen = {}, cats = [];
  l.blocks.forEach(function(b){ if(!seen[b[0]]){ seen[b[0]] = true; cats.push(b[0]); } });
  var outputs = l.blocks.filter(function(b){ return blockRole(b[0]) === 'output'; }).map(function(b){ return b[0]; });
  var verify = outputs.length ? outputs.filter(function(n,i,a){ return a.indexOf(n) === i; }).join('、') : '屏幕、灯光或声音';
  return '<section class="platform-workflow"><div class="workflow-head"><div><span>MBLOCK → CYBERPI</span><h4>本课统一实施流程</h4></div><p>编程在 mBlock 完成，CyberPi 用来接收真实输入并验证结果。</p></div><div class="workflow-grid">'+
    '<article><i>01</i><b>添加设备</b><p>在 mBlock 添加“童芯派”，用数据线连接，看到“设备已连接”。</p></article>'+
    '<article><i>02</i><b>选择模式</b><p>先用在线模式边搭边测；作品稳定后，可切换上传模式独立运行。</p></article>'+
    '<article><i>03</i><b>找到积木</b><p>本课会用到：'+esc(cats.join('、'))+'。</p></article>'+
    '<article><i>04</i><b>分段搭建</b><p>按“真实输入—逻辑处理—硬件输出”连接，每完成一段就运行一次。</p></article>'+
    '<article><i>05</i><b>实体触发</b><p>操作 CyberPi 的按钮、摇杆或传感器，不用舞台角色代替硬件输入。</p></article>'+
    '<article><i>06</i><b>真机验收</b><p>观察 CyberPi 的'+esc(verify)+'反馈，并记录一次修改前后的差异。</p></article>'+
  '</div></section>';
}
function sampleTestLab(l){
  var s = taskSpec(l);
  var playIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m9 7 8 5-8 5V7z"/><circle cx="12" cy="12" r="9"/></svg>';
  var searchIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/><path d="M8 10.5h5M10.5 8v5"/></svg>';
  var upgradeIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20V6M6 12l6-6 6 6"/><path d="M5 20h14"/></svg>';
  var testCases = s.tests.slice(0,3).map(function(r){ return '<div class="play-case"><span>这样试</span><b>'+esc(r[0])+'</b><i>看看是不是</i><p>'+esc(r[1])+'</p></div>'; }).join('');
  var bugCards = s.bugs.slice(0,2).map(function(n){ return '<div class="bug-clue"><b>'+esc(n[0])+'</b><p>'+esc(n[1])+'</p></div>'; }).join('');
  return '<section class="sample-test-lab kid-test-lab"><div class="sample-test-head"><div><span>PLAY LAB · 试玩站</span><h4>试一试，找一找，再升级</h4></div><p>每次只改一个地方，马上在 CyberPi 上再试一次。</p></div><div class="kid-test-route">'+
    '<article class="kid-test-card try-card"><header><i>'+playIcon+'</i><div><small>第 1 步</small><b>先试一试</b></div></header><p class="card-lead">换几种按法或环境，看看作品会怎样回应。</p><div class="play-cases">'+testCases+'</div></article>'+
    '<article class="kid-test-card find-card"><header><i>'+searchIcon+'</i><div><small>第 2 步</small><b>不对就找一找</b></div></header><p class="card-lead">先找到没反应的那一步，不用把所有积木都拆掉。</p><div class="bug-clues">'+bugCards+'</div></article>'+
    '<article class="kid-test-card upgrade-card"><header><i>'+upgradeIcon+'</i><div><small>第 3 步</small><b>改一处，再试一次</b></div></header><p class="card-lead">挑一个数字、颜色、声音或判断规则，改完马上运行。</p><div class="upgrade-action"><span>说一说</span><p>'+esc(s.reflection[0])+'</p></div><div class="upgrade-action"><span>小目标</span><p>我能说出改了哪里，以及 CyberPi 的回应有什么不同。</p></div></article>'+
  '</div></section>';
}

function renderCourse(id){
  var l = COURSE[id];
  if(!l){ go('#/home'); return; }
  var ch = CHAPTERS[l.ch-1];
  var d = DB.get();
  var rec = DB.lessonRec(d, id);

  document.getElementById('courseTop').style.setProperty('--ch-color', ch.color);
  document.getElementById('view-course').style.setProperty('--ch-color', ch.color);
  document.getElementById('ctNo').textContent = fmtNo(id);
  document.getElementById('ctTitle').textContent = l.title;
  document.getElementById('ctSub').textContent = '第'+ch.id+'章 · '+ch.name+' ｜ '+l.theme;
  var pct = rec.done ? 100 : Math.round(rec.correct / l.quiz.length * 100);
  document.getElementById('ctRing').style.setProperty('--p', pct);
  document.getElementById('ctRingPct').textContent = rec.done ? '✓' : pct + '%';
  document.getElementById('ctProgTxt').textContent = rec.done ? '本课已完成' : '完成问答点亮进度';

  document.getElementById('courseTabs').innerHTML = TABS.map(function(t, i){
    return '<button class="tab-btn'+(i===0?' active':'')+'" data-tab="'+t.key+'" aria-selected="'+(i===0?'true':'false')+'" aria-controls="panel-'+t.key+'" onclick="switchTab(this)">' +
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
  document.querySelectorAll('#courseTabs .tab-btn').forEach(function(b){ b.classList.remove('active'); b.setAttribute('aria-selected','false'); });
  btn.classList.add('active');
  btn.setAttribute('aria-selected','true');
  var key = btn.getAttribute('data-tab');
  document.querySelectorAll('#coursePanels .tab-panel').forEach(function(p){ p.classList.remove('active'); });
  document.getElementById('panel-'+key).classList.add('active');
}
function goStep(key){
  var btn = document.querySelector('#courseTabs [data-tab="'+key+'"]');
  if(btn){ switchTab(btn); window.scrollTo(0, document.getElementById('courseTop').offsetHeight || 0); }
}
function nextStepButton(key, label){
  return '<div class="panel-next"><button class="btn" onclick="goStep(\''+key+'\')"><span>下一步</span>'+label+'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button></div>';
}
function blockRole(cat){
  if(['事件','传感','网络/AI','扩展'].indexOf(cat) >= 0) return 'input';
  if(['显示','外观','灯','声音','运动'].indexOf(cat) >= 0) return 'output';
  return 'logic';
}
function blockRoleLabel(cat){
  var r = blockRole(cat);
  return r === 'input' ? '输入 / 启动' : (r === 'output' ? '反馈 / 输出' : '处理 / 判断');
}
function blockFamilyExplorer(l){
  var seen = {}, cats = [];
  l.blocks.forEach(function(b){ if(!seen[b[0]]){ seen[b[0]] = true; cats.push(b[0]); } });
  return '<div class="family-explorer"><div class="family-title"><b>同类型积木还能做什么？</b><span>点击积木类型展开</span></div>' + cats.map(function(cat, i){
    var items = BLOCK_FAMILIES[cat] || ['更多同类积木将在工程验证后补充'];
    var color = CAT_COLOR[cat] || 'var(--primary)';
    return '<details class="block-family"'+(i===0?' open':'')+'><summary><i style="background:'+color+'"></i><b>'+esc(cat)+'类积木</b><span>'+items.length+' 个常用积木</span></summary><div class="family-items">'+items.map(function(n){ return '<span style="--family-color:'+color+'">'+esc(n)+'</span>'; }).join('')+'</div></details>';
  }).join('') + '</div>';
}

/* ---- 面板：课程导入 ---- */
function panelIntro(l, ch){
  var pad = l.id < 10 ? '0' + l.id : '' + l.id;
  var steps = [
    {ico:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>', t:'读故事', p:'回顾绘本第'+l.echoId+'课《'+l.echoTitle+'》'},
    {ico:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 9h.01M16 9h.01M8 15h8"/></svg>', t:'写程序', p:'在 mBlock 中搭建AI硬件程序'},
    {ico:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="12" rx="3"/><circle cx="12" cy="12" r="3.2"/><path d="M7 6V4h10v2"/></svg>', t:'测一测', p:'连接 CyberPi，边搭建边在真机验证'}
  ];
  return '<div class="panel-card tab-panel active" id="panel-intro">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[0].icon+'</span>课程导入 · 绘本呼应</h3>' +
    '<div class="intro-hero">' +
      '<div class="intro-cover"><img src="'+lessonAsset(l.id)+'" alt="'+esc(l.title)+'"></div>' +
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
    sampleDriving(l) +
    '<div class="time-plan"><span>故事 10%</span><span>AI编程 55%</span><span>硬件交互 20%</span><span>挑战复盘 15%</span></div>' +
    '<div class="flow-steps">' + steps.map(function(s){
      return '<div class="flow-step"><div class="fs-ico">'+s.ico+'</div><b>'+s.t+'</b><p>'+s.p+'</p></div>';
    }).join('') + '</div>' + nextStepButton('know','查看学习目标') + '</div>';
}

/* ---- 面板：AI 知识点 ---- */
function panelKnow(l, ch){
  var goalNames = ['看懂它','搭出来','试明白'];
  var goals = l.knowledge.map(function(k, i){
    return '<article class="goal-stage"><span class="goal-stage-no">0'+(i+1)+'</span><div><small>'+goalNames[i%goalNames.length]+'</small><strong>'+esc(k)+'</strong></div></article>';
  }).join('');
  return '<div class="panel-card tab-panel" id="panel-know">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[1].icon+'</span>本节学习目标</h3>' +
    '<figure class="goal-visual"><div class="goal-picture"><img src="'+lessonAsset(l.id)+'" alt="'+esc(l.title)+'学习目标图示"><span>'+fmtNo(l.id)+'</span></div>'+
      '<div class="goal-map"><div class="goal-map-head"><span>TODAY · 今天学什么</span><h4>'+esc(l.theme)+'</h4></div>'+
      '<div class="goal-stages">'+goals+'</div></div></figure>' + nextStepButton('blocks','进入积木程序') + '</div>';
}

/* ---- 面板：编程积木 ---- */
function panelBlocks(l, ch){
  var rows = '';
  var roleCount = {input:0,logic:0,output:0};
  l.blocks.forEach(function(b, i){
    var color = CAT_COLOR[b[0]] || 'var(--primary)';
    var role = blockRole(b[0]); roleCount[role]++;
    rows += '<div class="blk-row program-node"><span class="node-index">'+(i+1)+'</span><span class="blk-lab">'+blockRoleLabel(b[0])+'</span>' +
      '<span class="blk" style="background:'+color+'"><span class="blk-cat">'+b[0]+'</span>'+esc(b[1])+'</span><span class="node-check">检查参数</span></div>';
  });
  var proof = sampleMediaStudio(l);
  var first = l.blocks.find(function(b){ return blockRole(b[0]) === 'input'; }) || l.blocks[0];
  var logicBlocks = l.blocks.filter(function(b){ return blockRole(b[0]) === 'logic'; });
  var middle = l.blocks.find(function(b){ return b[0] === '控制' || b[0] === '运算'; }) || logicBlocks[Math.min(1,logicBlocks.length-1)] || l.blocks[Math.floor(l.blocks.length/2)];
  var outputs = l.blocks.filter(function(b){ return blockRole(b[0]) === 'output'; });
  var last = outputs[outputs.length-1] || l.blocks[l.blocks.length-1];
  var kidHook = l.programHook || ('团团想把 CyberPi 变成“'+l.projName+'”。它会在什么时候收到消息，又会怎样回答？先猜一猜。');
  var kidGoal = l.programGoal || ('今天把“'+l.projName+'”做出来。先搭一小段就试一次，看看 CyberPi 是不是真的听懂了。');
  var kidWatch = l.programWatch || ('程序跑起来后别急着翻页。动手试一试：'+(l.programObserve || ('“'+l.theme+'”会让结果发生什么变化？')));
  return '<div class="panel-card tab-panel" id="panel-blocks">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[2].icon+'</span>本课积木程序</h3>' +
    '<div class="program-summary"><div><span>PROGRAM BLUEPRINT</span><h4>'+esc(l.projName)+'</h4><p>先读懂程序为什么这样连接，再动手搭建。</p></div><div class="program-metrics"><b>'+l.blocks.length+'<small>块核心积木</small></b><b>'+roleCount.input+'<small>输入/启动</small></b><b>'+roleCount.logic+'<small>逻辑处理</small></b><b>'+roleCount.output+'<small>反馈输出</small></b></div></div>'+
    '<section class="program-lesson-brief"><div class="program-brief-head"><span>团团和点点的编程小剧场</span><h4>先玩明白，再动手搭</h4><p>别急着找积木。先听故事，猜一猜，再让 CyberPi 真的动起来。</p></div><div class="program-brief-grid">'+
      '<article class="brief-guess"><i>想</i><div><b>先猜猜</b><p>'+esc(kidHook)+'</p></div></article>'+
      '<article class="brief-build"><i>做</i><div><b>今天做这个</b><p>'+esc(kidGoal)+'</p></div></article>'+
      '<article class="brief-watch"><i>看</i><div><b>小眼睛看这里</b><p>'+esc(kidWatch)+'</p></div></article>'+
    '</div></section>'+
    '<div class="program-runtime"><div class="runtime-head"><b>程序模块地图</b><span>每个模块先单独试玩，再把它们连起来</span></div><div class="runtime-track">'+
      '<article class="runtime-card input"><span>01 · 触发模块</span><b>'+esc(first[1])+'</b><small>负责接收事件或传感信息</small></article><i>→</i>'+
      '<article class="runtime-card logic"><span>02 · 思考模块</span><b>'+esc(middle[1])+'</b><small>负责变量、判断、运算或循环</small></article><i>→</i>'+
      '<article class="runtime-card output"><span>03 · 反馈模块</span><b>'+esc(last[1])+'</b><small>负责屏幕、灯光、声音或动作</small></article></div></div>'+
    '<div class="program-workbench"><section><div class="workbench-title"><div><span>搭建区</span><b>按顺序连接核心积木</b></div><small>共 '+l.blocks.length+' 步</small></div><div class="blk-list program-sequence">'+rows+'</div></section>'+
      '<aside class="program-guide"><span class="guide-kicker">读程序三问</span><div><i>1</i><p><b>什么时候开始？</b><small>找到事件、传感或AI输入。</small></p></div><div><i>2</i><p><b>程序怎样处理？</b><small>关注执行顺序、条件、变量、运算与循环。</small></p></div><div><i>3</i><p><b>结果在哪里出现？</b><small>观察 CyberPi 的屏幕、灯光、声音或运动反馈。</small></p></div><div class="guide-tip">设备保持连接，搭完一小段就在真机上运行一次，更容易发现连接或参数问题。</div></aside></div>'+
    proof + '<div class="tip-box"><b>mBlock + CyberPi 流程：</b>先添加并连接童芯派，确认模式，再按“事件输入—逻辑处理—硬件输出”搭建；每完成一段就用实体按钮或传感器在 CyberPi 上验证。</div>' + blockFamilyExplorer(l) + nextStepButton('demo','开始编程任务') + '</div>';
}

/* ---- 面板：CyberPi 演示 ---- */
function panelDemo(l, ch){
  var task = l.transfer || {name:l.projName, eff:l.projEff, steps:l.steps, challenge:l.challenge};
  var phaseNames = ['准备','搭建','连接','测试','改进'];
  var sample = sampleOf(l);
  if(sample && sample.phases) phaseNames = sample.phases;
  var success = sample && sample.success ? sample.success : ['程序能按步骤完整运行','硬件能给出可观察的反馈','我能解释“'+l.theme+'”怎样体现在作品中'];
  return '<div class="panel-card tab-panel" id="panel-demo">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[3].icon+'</span>本节AI硬件编程任务</h3>' +
    '<div class="transfer-banner"><span>举一反三 · 基于“'+esc(l.projName)+'”进行改造</span><b>不是重做一遍，而是保留核心逻辑、改变使用情境</b></div>'+
    '<div class="task-hero proj-card"><div class="task-hero-copy"><span class="task-kicker">MISSION · '+fmtNo(l.id)+' 迁移任务</span><div class="p-name"><span class="t-ico" style="background:hsl(0 0% 100% / .22)">'+TABS[3].icon+'</span>'+esc(task.name)+'</div><div class="p-eff">'+esc(task.eff)+'</div></div>'+
      '<div class="task-stamp"><b>'+task.steps.length+'</b><span>个改造步骤</span><small>'+esc(l.theme)+'</small></div></div>'+
    platformWorkflow(l) + sampleTaskLab(l) +
    '<div class="task-dashboard"><section class="task-main"><div class="task-section-head"><div><span>POWER-UP PLAN</span><h4>创意升级路线</h4></div><p>跟着步骤，让作品变得更有趣</p></div><div class="steps-list task-steps">' + task.steps.map(function(s, i){
      var blockIndex = task.steps.length < 2 ? 0 : Math.round(i * (l.blocks.length - 1) / (task.steps.length - 1));
      var stepBlock = l.blocks[blockIndex] || l.blocks[0] || ['事件',''];
      var stepColor = CAT_COLOR[stepBlock[0]] || 'var(--primary)';
      return '<div class="step-item" style="--step-color:'+stepColor+'"><span class="s-no">'+(i+1)+'</span><div class="step-copy"><small>'+phaseNames[Math.min(i,phaseNames.length-1)]+'阶段</small><p>'+esc(s)+'</p></div><span class="step-block-tag">'+esc(stepBlock[0])+'积木</span></div>';
    }).join('') + '</div></section>'+
    '<aside class="task-side"><div class="task-side-card materials"><span>HARDWARE</span><h4>本课工具箱</h4><div class="hw-chips">'+ l.hardware.map(function(h){ return '<span class="hw-chip">'+esc(h)+'</span>'; }).join('') + '</div></div>'+
      '<div class="task-side-card criteria"><span>SUCCESS CHECK</span><h4>成功标准</h4><ul>'+success.map(function(n){ return '<li>'+esc(n)+'</li>'; }).join('')+'</ul></div></aside></div>'+
    '<div class="task-preview"><span>完成后的加分挑战</span><p>'+esc(task.challenge)+'</p></div>' + nextStepButton('challenge','进入试玩与升级') + '</div>';
}

/* ---- 面板：动手挑战 ---- */
function panelChallenge(l, ch){
  var task = l.transfer || {challenge:l.challenge};
  return '<div class="panel-card tab-panel" id="panel-challenge">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[4].icon+'</span>试玩、找错和升级</h3>' +
    '<div class="challenge-box"><span class="c-tag">团团和点点的试玩站</span><p>让 CyberPi 跑起来，多试几种玩法。没成功也没关系：看一看、改一处，再试一次。</p></div>' +
    sampleTestLab(l) +
    (l.tip ? '<div class="tip-box"><b>团团小提醒：</b>'+esc(l.tip)+'</div>' : '') + nextStepButton('quiz','去闯关答题') + '</div>';
}

/* ---- 面板：知识问答 ---- */
function panelQuiz(l, ch){
  return '<div class="panel-card tab-panel" id="panel-quiz">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[5].icon+'</span>进阶挑战与随堂问答</h3>' +
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
  svg += '<defs>' +
    '<linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBFAFF"/><stop offset=".52" stop-color="#EDE9FA"/><stop offset="1" stop-color="#DCEEFF"/></linearGradient>' +
    '<linearGradient id="screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#203D66"/><stop offset="1" stop-color="#0B1E38"/></linearGradient>' +
    '<filter id="boardShadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="9" stdDeviation="8" flood-color="#51456F" flood-opacity=".18"/></filter>' +
    '<filter id="partShadow" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="4" stdDeviation="3" flood-color="#51456F" flood-opacity=".24"/></filter>' +
    '<filter id="activeGlow" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#8B5CF6" flood-opacity=".8"/></filter>' +
    '</defs>';
  svg += '<circle cx="43" cy="35" r="22" fill="#DDF7F1" opacity=".75"/><circle cx="444" cy="39" r="29" fill="#FCE3F0" opacity=".7"/><circle cx="437" cy="229" r="19" fill="#FFF0C8" opacity=".78"/>';
  svg += '<rect x="14" y="14" width="452" height="242" rx="31" fill="url(#bd)" stroke="#FFFFFF" stroke-width="3" filter="url(#boardShadow)"/>';
  svg += '<rect x="24" y="24" width="432" height="222" rx="23" fill="none" stroke="#CFC5E4" stroke-width="1.4" stroke-dasharray="5 6"/>';
  svg += '<rect x="34" y="30" width="118" height="24" rx="12" fill="#FFFFFF" opacity=".88"/><text x="46" y="46" font-size="11" font-weight="800" fill="#6E5A91" letter-spacing=".8">CyberPi · 童芯派</text>';
  svg += '<rect x="379" y="31" width="66" height="22" rx="11" fill="#FFFFFF" opacity=".9"/><text x="412" y="46" text-anchor="middle" font-size="9.5" font-weight="800" fill="#7C3AED">点击部件</text>';

  svg += '<g class="hotspot" data-hw="display" onclick="hwInfo(\'display\')"><rect x="145" y="47" width="190" height="122" rx="16" fill="#FFFFFF" opacity=".72"/><rect x="150" y="52" width="180" height="112" rx="11" fill="url(#screen)" stroke="#FFFFFF" stroke-width="2" filter="url(#partShadow)"/>' +
    '<circle cx="196" cy="96" r="7" fill="#FFD166"/><circle cx="250" cy="96" r="7" fill="#FFD166"/>' +
    '<path d="M196 130 q28 26 54 0" stroke="#7EE0A3" stroke-width="6" fill="none" stroke-linecap="round"/>' +
    '<text x="240" y="40" text-anchor="middle" font-size="11" font-weight="800" fill="#2E5B92">显示屏</text></g>';

  svg += '<g class="hotspot" data-hw="joystick" onclick="hwInfo(\'joystick\')"><circle cx="70" cy="88" r="27" fill="#FFFFFF" opacity=".7"/><circle cx="70" cy="88" r="19" fill="#fff" stroke="#7FA8D8" stroke-width="2.5" filter="url(#partShadow)"/>' +
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
  document.querySelectorAll('#hwSvgCard .hotspot').forEach(function(el){
    el.classList.toggle('active', el.getAttribute('data-hw') === key);
  });
  document.getElementById('hwInfo').innerHTML =
    '<div class="hi-kicker">当前选中部件</div>' +
    '<div class="hi-name"><span class="hi-dot">●</span>'+p.name+'</div>' +
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
  if(e.key === 'Escape' && document.getElementById('imgLightbox').style.display !== 'none'){ closeImgLightbox(); }
  if(document.getElementById('imgLightbox').style.display !== 'none' && (e.key === '+' || e.key === '=')){ changeImageZoom(.25); }
  if(document.getElementById('imgLightbox').style.display !== 'none' && e.key === '-'){ changeImageZoom(-.25); }
});
