# -*- coding: utf-8 -*-
import io

path = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
with io.open(path, 'r', encoding='utf-8') as f:
    src = f.read()

# === 1. 在 CAT_DESC 后面添加 BLOCK_LIBRARY 积木知识库 ===
cat_desc_end = """  '网络/AI':'AI和联网功能的"魔法积木"。包括语音识别等，让CyberPi能听懂人话。'
};"""

block_library = """  '网络/AI':'AI和联网功能的"魔法积木"。包括语音识别等，让CyberPi能听懂人话。'
};
var BLOCK_LIBRARY = {
  '事件': [
    {n:'当 CyberPi 开机时', d:'程序的入口，CyberPi一开机就从这里开始运行下面的积木。'},
    {n:'当按钮 A 被按下时', d:'每次按下按钮A，就执行一次挂在下面的积木，常用作用户输入触发。'},
    {n:'当按钮 B 被按下时', d:'每次按下按钮B触发，常和按钮A配合（一个确认、一个返回）。'},
    {n:'当摇杆向上/下/左/右时', d:'摇杆拨到指定方向时触发，适合做方向控制类游戏。'},
    {n:'当收到消息 [消息] 时', d:'收到指定广播消息时触发，用于程序不同部分之间通信。'}
  ],
  '控制': [
    {n:'等待 [1] 秒', d:'程序暂停指定秒数，什么都不做，时间到了继续往下执行。'},
    {n:'重复执行 [10] 次', d:'把里面的积木重复执行指定次数，做完继续往下。'},
    {n:'重复执行', d:'把里面的积木无限循环执行，永远做下去（除非程序停止）。'},
    {n:'如果 [条件] 那么', d:'检查条件是否满足，满足就执行里面的积木，不满足就跳过。'},
    {n:'如果 [条件] 那么…否则', d:'条件满足执行第一组积木，不满足执行「否则」里的积木，二选一。'},
    {n:'重复执行直到 [条件]', d:'反复执行里面的积木，直到条件满足才停下来，适合"一直做到成功"。'},
    {n:'停止全部脚本', d:'立刻停止整个程序的运行。'}
  ],
  '显示': [
    {n:'显示文字 [你好]', d:'在屏幕上显示一行文字，是CyberPi跟人"说话"的主要方式。'},
    {n:'显示数字 [0]', d:'在屏幕上显示一个数字，数字会更新覆盖之前的内容。'},
    {n:'显示变量 [变量]', d:'把变量里存的值取出来显示在屏幕上，变量变了显示也跟着变。'},
    {n:'清空屏幕', d:'把屏幕上所有内容擦掉，变成黑屏，准备显示新内容。'},
    {n:'在 x:[0] y:[0] 绘制像素点', d:'在屏幕指定坐标处点亮一个像素点，坐标从左上角(0,0)开始数。'},
    {n:'绘制矩形/圆形/线', d:'在屏幕上绘制基本几何图形，可以指定位置、大小和颜色。'}
  ],
  '灯': [
    {n:'RGB灯 亮起 [颜色]', d:'把5颗RGB灯调成指定颜色并亮起，灯立刻发光。'},
    {n:'RGB灯 熄灭', d:'把所有RGB灯关掉，灯不发光。'},
    {n:'设置RGB灯 红:[0]绿:[0]蓝:[0]', d:'按红绿蓝三个通道亮度值(0-255)混合出颜色，配比不同颜色就不同。'},
    {n:'设置第[N]颗灯 颜色', d:'只控制指定的某一颗灯，5颗灯可以分别显示不同颜色。'},
    {n:'设置RGB灯亮度 [0-100]', d:'调节所有灯的整体亮度，0最暗、100最亮。'}
  ],
  '声音': [
    {n:'播放音符 [C4] [0.5]拍', d:'播放一个指定音高和时长的音符，多个音符可以拼成旋律。'},
    {n:'播放音效 [提示音]', d:'播放内置的短音效（提示音、奖励音、错误音等），用来给反馈。'},
    {n:'朗读 [文字]', d:'把文字变成说话声读出来（语音合成），是AI的"嘴巴"，需要联网。'},
    {n:'设置音量 [0-100]', d:'调节扬声器的整体音量，0静音、100最大声。'},
    {n:'停止所有声音', d:'立刻停止正在播放的所有声音和音乐。'}
  ],
  '传感': [
    {n:'按钮 A 是否按下', d:'检测按钮A当前有没有被按下，返回"真"或"假"，用于条件判断。'},
    {n:'摇杆 X 轴 / Y 轴', d:'读取摇杆当前的位置数值，左右拨X轴变化、上下拨Y轴变化。'},
    {n:'环境光强度', d:'读取当前环境光线的亮暗程度，返回0-100的数字，越亮数字越大。'},
    {n:'声音强度 / 音量', d:'读取麦克风检测到的周围声音大小，声音越大数字越大。'},
    {n:'加速度 X/Y/Z 轴', d:'读取加速度传感器数值，能感知摇晃、倾斜和移动方向。'},
    {n:'陀螺仪角度', d:'读取CyberPi的倾斜角度，能知道设备是正着放还是歪着放。'}
  ],
  '运算': [
    {n:'[1] + [1] / - / × / ÷', d:'加减乘除四则运算，把两个数字算出结果。'},
    {n:'随机数 [1] 到 [10]', d:'随机生成一个指定范围内的整数，每次运行结果可能不同。'},
    {n:'[1] < [2] / = / >', d:'比较两个数字的大小或是否相等，结果为"真"或"假"。'},
    {n:'[条件] 且 [条件]', d:'逻辑"与"：两个条件都满足时结果才为真，缺一不可。'},
    {n:'[条件] 或 [条件]', d:'逻辑"或"：只要有一个条件满足结果就为真。'},
    {n:'不 [条件]', d:'逻辑"非"：把条件结果反过来，真变假、假变真。'},
    {n:'连接 [文字1] [文字2]', d:'把两段文字拼在一起变成一段，比如"你好"+"世界"="你好世界"。'}
  ],
  '变量': [
    {n:'建立变量 [名字]', d:'创建一个有名字的"小抽屉"，用来存数字或文字，程序运行中可随时取用。'},
    {n:'将 [变量] 设为 [值]', d:'把变量里的内容改成指定的值，覆盖原来的内容。'},
    {n:'将 [变量] 增加 [1]', d:'把变量的值加上指定数量，比如加1就是每次多1，常用于计数。'},
    {n:'显示变量 [变量]', d:'在屏幕上显示变量当前的值，变量变了显示也跟着更新。'}
  ],
  '自制': [
    {n:'定义自制积木 [名字]', d:'把一串积木打包成一个新的自定义积木，起个好记的名字。'},
    {n:'调用自制积木 [名字]', d:'直接使用之前定义好的自制积木，执行它里面打包的整串步骤。'}
  ],
  '扩展': [
    {n:'机器学习2.0 · 训练', d:'采集样本数据训练AI模型，让机器学会认识不同类别（如拍手/吹口哨）。'},
    {n:'机器学习2.0 · 识别', d:'用训练好的模型识别当前输入属于哪个类别，返回识别结果标签。'},
    {n:'语音识别', d:'录一段音发送到云端识别成文字（语音转文字），需要联网。'},
    {n:'获取天气数据', d:'从网络获取指定城市的天气信息（温度、湿度等），需要联网。'}
  ],
  '网络/AI': [
    {n:'识别语音 [2]秒', d:'录制指定秒数的声音，发送到云端识别成文字，需要联网。'},
    {n:'语音识别结果', d:'取出上一次语音识别得到的文字结果，用来做后续判断和处理。'},
    {n:'朗读 [文字]', d:'把文字变成说话声读出来（语音合成），AI的"嘴巴"，需要联网。'}
  ]
};
function toggleCat(btn, cat){
  var panel = btn.nextElementSibling;
  var isOpen = panel.style.display === 'block';
  // 关闭所有
  document.querySelectorAll('.cat-expand').forEach(function(p){ p.style.display='none'; });
  document.querySelectorAll('.cat-btn').forEach(function(b){ b.classList.remove('open'); });
  if(!isOpen){
    panel.style.display = 'block';
    btn.classList.add('open');
  }
}"""

if cat_desc_end in src:
    src = src.replace(cat_desc_end, block_library, 1)
    print("OK: added BLOCK_LIBRARY and toggleCat")
else:
    print("FAIL: cat_desc_end not found")

# === 2. 修改 panelBlocks 函数 ===
old_panel_blocks = """function panelBlocks(l, ch){
  var catsUsed = [];
  l.blocks.forEach(function(b){ if(catsUsed.indexOf(b[0])<0) catsUsed.push(b[0]); });
  var catIntro = '<div class="blk-cat-intro">';
  catsUsed.forEach(function(c){
    var color = CAT_COLOR[c] || 'var(--primary)';
    catIntro += '<div class="bci-item"><span class="bci-dot" style="background:'+color+'"></span><b>'+c+'</b><p>'+(CAT_DESC[c]||'')+'</p></div>';
  });
  catIntro += '</div>';
  var rows = '';
  l.blocks.forEach(function(b){
    var color = CAT_COLOR[b[0]] || 'var(--primary)';
    rows += '<div class="blk-card">' +
      '<div class="blk-card-top"><span class="blk-lab" style="background:'+color+'">'+b[0]+'</span>' +
      '<span class="blk" style="background:'+color+'"><span class="blk-cat">'+b[0]+'</span>'+esc(b[1])+'</span></div>' +
      '<div class="blk-desc">'+blockDesc(b[0], b[1])+'</div></div>';
  });
  return '<div class="panel-card tab-panel" id="panel-blocks">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[2].icon+'</span>用到的 mBlock 积木</h3>' +
    '<div class="blk-guide"><div class="bg-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></div>' +
    '<div><b>什么是积木编程？</b><p>mBlock 用彩色积木块代替打字写代码。不同颜色代表不同功能（事件=黄色、控制=橙色、显示=紫色…），把积木从上到下拼在一起，程序就按顺序执行。就像搭乐高一样，拼对了 CyberPi 就听话。</p></div></div>' +
    catIntro +
    '<div class="blk-cards">'+rows+'</div>' +
    '<div class="tip-box">在 mBlock 5 中选择「CyberPi」设备，从左侧对应分类里拖出这些积木，像拼乐高一样把它们上下接起来。</div>' + nextStageBtn('下一环节：看演示') + '</div>';
}"""

new_panel_blocks = """function panelBlocks(l, ch){
  var catsUsed = [];
  l.blocks.forEach(function(b){ if(catsUsed.indexOf(b[0])<0) catsUsed.push(b[0]); });
  var rows = '';
  l.blocks.forEach(function(b){
    var color = CAT_COLOR[b[0]] || 'var(--primary)';
    rows += '<div class="blk-card">' +
      '<div class="blk-card-top">' +
      '<span class="blk" style="background:'+color+'"><span class="blk-cat">'+b[0]+'</span>'+esc(b[1])+'</span></div>' +
      '<div class="blk-desc">'+blockDesc(b[0], b[1])+'</div></div>';
  });
  // 下方：分类探索按钮（可点击展开）
  var catExplore = '<div class="cat-explore"><div class="ce-title"><span class="ce-ico">📚</span><b>积木分类探索</b><span class="ce-hint">点击分类查看该分类的常用积木</span></div>';
  catsUsed.forEach(function(c){
    var color = CAT_COLOR[c] || 'var(--primary)';
    var lib = BLOCK_LIBRARY[c] || [];
    var items = '';
    lib.forEach(function(item){
      items += '<div class="ce-item"><span class="ce-blk" style="background:'+color+'">'+esc(item.n)+'</span><p>'+esc(item.d)+'</p></div>';
    });
    catExplore += '<button class="cat-btn" style="border-left:4px solid '+color+'" onclick="toggleCat(this,\\''+c+'\\')">' +
      '<span class="cb-dot" style="background:'+color+'"></span><b>'+c+'</b>' +
      '<span class="cb-desc">'+(CAT_DESC[c]||'')+'</span>' +
      '<span class="cb-arrow">▸</span></button>' +
      '<div class="cat-expand">'+items+'</div>';
  });
  catExplore += '</div>';
  return '<div class="panel-card tab-panel" id="panel-blocks">' +
    '<h3><span class="t-ico" style="background:'+ch.color+'">'+TABS[2].icon+'</span>用到的 mBlock 积木</h3>' +
    '<div class="blk-guide"><div class="bg-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></div>' +
    '<div><b>什么是积木编程？</b><p>mBlock 用彩色积木块代替打字写代码。不同颜色代表不同功能（事件=黄色、控制=橙色、显示=紫色…），把积木从上到下拼在一起，程序就按顺序执行。就像搭乐高一样，拼对了 CyberPi 就听话。</p></div></div>' +
    '<div class="blk-cards">'+rows+'</div>' +
    '<div class="tip-box">在 mBlock 5 中选择「CyberPi」设备，从左侧对应分类里拖出这些积木，像拼乐高一样把它们上下接起来。</div>' +
    catExplore +
    nextStageBtn('下一环节：看演示') + '</div>';
}"""

if old_panel_blocks in src:
    src = src.replace(old_panel_blocks, new_panel_blocks, 1)
    print("OK: replaced panelBlocks")
else:
    print("FAIL: old_panel_blocks not found")

# === 3. 添加新CSS样式 ===
old_css_marker = ".blk-desc{font-size:13px;color:var(--ink-2);line-height:1.7;padding-left:10px;border-left:3px solid var(--primary-100);padding-top:4px;padding-bottom:4px}"

new_css = """.blk-desc{font-size:13px;color:var(--ink-2);line-height:1.7;padding-left:10px;border-left:3px solid var(--primary-100);padding-top:4px;padding-bottom:4px}
.cat-explore{margin-top:24px;border-top:2px dashed var(--line);padding-top:20px}
.ce-title{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.ce-title .ce-ico{font-size:20px}
.ce-title b{font-size:16px;color:var(--ink)}
.ce-title .ce-hint{font-size:12px;color:var(--ink-2);font-weight:600;background:var(--accent);padding:4px 12px;border-radius:20px}
.cat-btn{width:100%;display:flex;align-items:center;gap:12px;background:#fff;border:1.5px solid var(--line);border-radius:12px;padding:14px 18px;margin-bottom:8px;cursor:pointer;transition:all .2s;text-align:left}
.cat-btn:hover{border-color:var(--primary);box-shadow:var(--shadow-sm);transform:translateY(-1px)}
.cat-btn.open{border-color:var(--primary);background:hsl(214 80% 98%)}
.cat-btn .cb-dot{width:14px;height:14px;border-radius:5px;flex:none}
.cat-btn b{font-size:14.5px;color:var(--ink);min-width:60px}
.cat-btn .cb-desc{font-size:12.5px;color:var(--ink-2);flex:1;line-height:1.5}
.cat-btn .cb-arrow{font-size:14px;color:var(--ink-2);transition:transform .2s;flex:none}
.cat-btn.open .cb-arrow{transform:rotate(90deg)}
.cat-expand{display:none;background:var(--accent);border-radius:0 0 12px 12px;padding:14px 18px;margin:-8px 0 10px 0;border:1.5px solid var(--line);border-top:none}
.ce-item{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px dashed var(--line)}
.ce-item:last-child{border-bottom:none}
.ce-blk{color:#fff;font-size:12.5px;font-weight:700;padding:6px 12px;border-radius:8px;flex:none;max-width:200px;line-height:1.3}
.ce-item p{font-size:12.5px;color:var(--ink-2);line-height:1.6;margin:0;flex:1}"""

if old_css_marker in src:
    src = src.replace(old_css_marker, new_css, 1)
    print("OK: added cat-explore CSS")
else:
    print("FAIL: old_css_marker not found")

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(src)
print("DONE: file saved")
