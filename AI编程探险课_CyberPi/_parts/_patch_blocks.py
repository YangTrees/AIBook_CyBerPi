# -*- coding: utf-8 -*-
import io, re

path = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
with io.open(path, 'r', encoding='utf-8') as f:
    src = f.read()

# === 积木分类说明字典 ===
CAT_DESC = {
    '事件': '程序的"启动开关"。当某个事情发生时（比如开机、按按钮），挂在它下面的积木就开始运行。',
    '控制': '程序的"大脑指挥官"。用「如果…就…」做判断、用「重复」做循环、用「等待」暂停，让程序有逻辑地运行。',
    '显示': 'CyberPi的"嘴巴和画笔"。在1.44寸彩屏上显示文字、数字，还能逐点亮起像素画图案。',
    '灯': 'CyberPi的"彩色表情"。5颗RGB灯可以调成红绿蓝任意颜色，亮灭和闪烁都能编程控制。',
    '声音': 'CyberPi的"嗓子"。既能播放音符和音效，也能用「朗读」积木把文字变成说话声（语音合成）。',
    '传感': 'CyberPi的"眼睛和耳朵"。读取光线强度、声音大小、摇杆位置、加速度倾斜，把外界信息变成数字。',
    '运算': '程序的"计算器"。做加减乘除、生成随机数、比较大小、用「且/或」组合多个条件。',
    '变量': '程序的"小抽屉"。建立一个有名字的格子来存数字或文字，可以随时取出来用、改掉、清零。',
    '自制': '程序的"打包盒"。把一串积木打包成一个有名字的新积木，下次用的时候直接拖出来，程序更整洁。',
    '扩展': 'AI和联网功能的"魔法积木"。包括机器学习训练/识别、语音识别等，需要联网使用。',
    '网络/AI': 'AI和联网功能的"魔法积木"。包括语音识别、语音合成等，让CyberPi能听懂人话、会说话。',
}

# === 积木作用说明生成器（根据分类+名称生成） ===
def block_desc(cat, name):
    n = name
    if cat == '事件':
        if '开机' in n: return '程序上传到CyberPi后，一开机就从这里开始运行，是整个程序的入口。'
        if '按钮' in n: return '当按下按钮A时，挂在下面的积木立刻执行一次，常用作用户输入触发。'
        return '当指定事件发生时，程序从这里开始运行。'
    if cat == '控制':
        if '重复执行直到' in n: return '反复执行里面的积木，直到满足某个条件才停下来，适合"一直做直到成功"的场景。'
        if '重复执行' in n and '次' in n:
            m = re.search(r'(\d+)\s*次', n)
            cnt = m.group(1) if m else 'N'
            return f'把里面的积木重复执行 {cnt} 次，做完就继续往下走。'
        if '重复执行' in n: return '把里面的积木无限重复执行，永远循环下去（除非程序停止）。'
        if '等待' in n:
            m = re.search(r'([\d.]+)\s*秒', n)
            t = m.group(1) if m else '一会儿'
            return f'程序暂停 {t} 秒，什么都不做，时间到了再继续往下执行。'
        if '否则' in n or '…否则' in n or '...否则' in n: return '如果条件满足就执行第一组积木，不满足就执行「否则」里的积木，二选一。'
        if '如果' in n: return '检查条件是否满足，满足就执行里面的积木，不满足就跳过，继续往下走。'
        return '控制程序的执行流程：判断、循环、暂停。'
    if cat == '显示':
        if '清空屏幕' in n and '绘制' in n: return '先把屏幕清空，然后在指定位置绘制图案，适合画完一帧再画下一帧。'
        if '清空屏幕' in n: return '把屏幕上所有内容擦掉，变成黑屏，准备显示新内容。'
        if '绘制像素' in n:
            if '位置' in n or '(x,y)' in n or '（x,y）' in n: return '在屏幕指定坐标(x,y)处点亮一个像素点，坐标从左上角(0,0)开始数。'
            if '笑脸' in n: return '用多个像素点在屏幕上拼出一个笑脸图案，每个像素就是一个小格子。'
            return '在屏幕上点亮一个像素点，像素是屏幕最小的发光格子。'
        if '显示' in n:
            if '数字' in n: return '在屏幕上显示一个数字（比如0或1），数字会更新覆盖之前的内容。'
            if '变量' in n: return '把变量里存的数字取出来，显示在屏幕上，变量变了显示也跟着变。'
            if '文字' in n: return '在屏幕上显示一行文字，是CyberPi跟人"说话"的主要方式。'
            return '在屏幕上显示指定的内容（文字、数字或变量值）。'
        return '控制屏幕显示内容。'
    if cat == '灯':
        if '熄灭' in n and '亮起' in n: return '切换RGB灯的亮灭状态，可以让灯在亮和灭之间来回切换。'
        if '熄灭' in n: return '把RGB灯关掉，灯不发光。'
        if '亮起' in n:
            if '红=' in n or '绿=' in n or '蓝=' in n: return '按红绿蓝三个通道的亮度值（0-255）混合出颜色，三种光配比不同颜色就不同。'
            colors = []
            for c in ['红色','绿色','蓝色','黄色']:
                if c in n: colors.append(c)
            if colors: return f'把RGB灯调成{ "、".join(colors) }，灯立刻亮起该颜色。'
            return '把RGB灯调成指定颜色并亮起。'
        return '控制5颗RGB彩灯的颜色和亮灭。'
    if cat == '声音':
        if '朗读' in n: return '把文字变成说话声读出来（语音合成），是AI的"嘴巴"，需要联网。'
        if '播放音符' in n: return '播放一个指定音高和时长的音符，比如C4音唱0.5拍，可以拼成旋律。'
        if '播放' in n:
            if '提示' in n: return '播放一段短促的提示音，用来提醒用户"操作成功了"。'
            if '奖励' in n: return '播放一段欢快的奖励音效，做对了就给点听觉鼓励。'
            return '播放指定的音效或声音。'
        return '控制扬声器播放声音。'
    if cat == '传感':
        if '环境光' in n: return '读取当前环境光线的亮暗程度，返回0-100的数字，越亮数字越大。'
        if '声音强度' in n or '音量' in n: return '读取麦克风检测到的声音大小，返回数字，声音越大数字越大。'
        if '加速度' in n or '摇一摇' in n or '陀螺仪' in n:
            if 'X' in n or 'x' in n: return '读取X轴加速度，左右倾斜时数值变化，向左摇为负数、向右摇为正数。'
            return '读取加速度传感器数值，能感知摇晃、倾斜和移动方向。'
        if '按钮' in n: return '检测按钮是否被按下，返回真/假，用来判断用户有没有操作。'
        return '读取传感器检测到的外界信息。'
    if cat == '运算':
        if '随机数' in n:
            m = re.search(r'(\d+)[-~到](\d+)', n)
            if m: return f'随机生成一个{m.group(1)}到{m.group(2)}之间的整数，每次运行结果可能不同。'
            return '随机生成一个指定范围内的整数。'
        if '增加' in n: return '把变量的值加上指定数量，比如加1就是每次多1，常用于计数。'
        if '总和' in n or '÷' in n or '/' in n: return '做除法运算，把总和除以份数得到平均值。'
        if '且' in n or '与' in n: return '逻辑"与"运算：两个条件都满足时结果才为真，缺一不可。'
        if '比较' in n or '>' in n or '<' in n or '=' in n: return '比较两个值的大小或是否相等，结果为真或假，用于条件判断。'
        if '综合分' in n or '×' in n or '*' in n or '+' in n: return '加权求和：每个输入乘以它的权重（重要程度），再加起来得到综合分。'
        return '做数学计算和逻辑运算。'
    if cat == '变量':
        if '建立变量' in n: return '创建一个有名字的"小抽屉"，用来存数字或文字，程序运行中可以随时取用和修改。'
        if '记录' in n: return '把当前读到的传感器数值存进变量，留着后面计算用（比如存3次光线值求平均）。'
        if '组' in n and '+1' in n: return '对应分组的计数器加1，每检测到一次该组就记一笔。'
        return '创建和使用变量存储数据。'
    if cat == '自制':
        if '定义' in n: return '把一串积木打包成一个新的自定义积木，起个好记的名字，以后直接调用这个名字就能执行整串步骤。'
        return '定义和调用自制积木。'
    if cat == '扩展':
        if '训练' in n:
            if '只训练' in n: return '只采集指定类别的声音样本进行训练（故意只练一类，用来演示数据偏见的问题）。'
            if '声音类别' in n: return '采集一类声音样本（比如拍手）作为训练数据，让机器学习认识这种声音。'
            return '采集样本数据训练机器学习模型。'
        if '识别' in n: return '用训练好的模型识别当前声音属于哪个类别，返回识别结果标签。'
        if '补训练' in n: return '补充采集之前缺少的类别样本重新训练，让模型学得更全面。'
        return '机器学习扩展功能。'
    if cat == '网络/AI':
        if '识别语音' in n: return '录一段音，发送到云端识别成文字（语音转文字），需要联网。'
        if '语音识别结果' in n: return '取出上一次语音识别得到的文字结果，用来做后续判断。'
        return 'AI语音识别功能。'
    return '一个编程积木。'

# 生成 BLOCK_DESC 字典的JS代码
desc_pairs = []
# 我们不在JS里硬编码所有积木，而是用一个函数根据分类和名称生成说明
# 但为了简单和可靠，直接在panelBlocks里用内联逻辑生成

# === 替换 panelBlocks 函数 ===
old_panel = """/* ---- 面板：编程积木 ---- */
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
    '<div class="tip-box">在 mBlock 5 中选择「CyberPi」设备，从对应分类里拖出这些积木，像拼乐高一样把它们接起来。</div>' + nextStageBtn('下一环节：看演示') + '</div>';
}"""

new_panel = """/* ---- 面板：编程积木 ---- */
var CAT_DESC = {
  '事件':'程序的"启动开关"。当某个事情发生时（比如开机、按按钮），挂在它下面的积木就开始运行。',
  '控制':'程序的"大脑指挥官"。用「如果…就…」做判断、用「重复」做循环、用「等待」暂停，让程序有逻辑地运行。',
  '显示':'CyberPi的"嘴巴和画笔"。在1.44寸彩屏上显示文字、数字，还能逐点亮起像素画图案。',
  '灯':'CyberPi的"彩色表情"。5颗RGB灯可以调成红绿蓝任意颜色，亮灭和闪烁都能编程控制。',
  '声音':'CyberPi的"嗓子"。既能播放音符和音效，也能用「朗读」积木把文字变成说话声（语音合成）。',
  '传感':'CyberPi的"眼睛和耳朵"。读取光线强度、声音大小、摇杆位置、加速度倾斜，把外界信息变成数字。',
  '运算':'程序的"计算器"。做加减乘除、生成随机数、比较大小、用「且/或」组合多个条件。',
  '变量':'程序的"小抽屉"。建立一个有名字的格子来存数字或文字，可以随时取出来用、改掉、清零。',
  '自制':'程序的"打包盒"。把一串积木打包成一个有名字的新积木，下次用的时候直接拖出来，程序更整洁。',
  '扩展':'AI和联网功能的"魔法积木"。包括机器学习训练/识别等，需要联网使用。',
  '网络/AI':'AI和联网功能的"魔法积木"。包括语音识别等，让CyberPi能听懂人话。'
};
function blockDesc(cat, name){
  var n = name;
  if(cat==='事件'){
    if(n.indexOf('开机')>=0) return '程序上传到CyberPi后，一开机就从这里开始运行，是整个程序的入口。';
    if(n.indexOf('按钮')>=0) return '当按下按钮A时，挂在下面的积木立刻执行一次，常用作用户输入触发。';
    return '当指定事件发生时，程序从这里开始运行。';
  }
  if(cat==='控制'){
    if(n.indexOf('重复执行直到')>=0) return '反复执行里面的积木，直到满足某个条件才停下来，适合"一直做直到成功"。';
    if(n.indexOf('重复执行')>=0 && n.indexOf('次')>=0){ var m=n.match(/(\\d+)\\s*次/); return '把里面的积木重复执行 '+(m?m[1]:'N')+' 次，做完继续往下。'; }
    if(n.indexOf('重复执行')>=0) return '把里面的积木无限重复执行，永远循环下去。';
    if(n.indexOf('等待')>=0){ var m2=n.match(/([\\d.]+)\\s*秒/); return '程序暂停 '+(m2?m2[1]:'一会儿')+' 秒，时间到了再继续。'; }
    if(n.indexOf('否则')>=0) return '条件满足就执行第一组，不满足就执行「否则」里的积木，二选一。';
    if(n.indexOf('如果')>=0) return '检查条件是否满足，满足就执行里面的积木，不满足就跳过。';
    return '控制程序的执行流程。';
  }
  if(cat==='显示'){
    if(n.indexOf('清空屏幕')>=0 && n.indexOf('绘制')>=0) return '先清屏再在指定位置绘制图案，适合画完一帧再画下一帧。';
    if(n.indexOf('清空屏幕')>=0) return '把屏幕上所有内容擦掉，变成黑屏，准备显示新内容。';
    if(n.indexOf('绘制像素')>=0){
      if(n.indexOf('位置')>=0||n.indexOf('x,y')>=0) return '在屏幕指定坐标(x,y)处点亮一个像素点，从左上角(0,0)开始数。';
      if(n.indexOf('笑脸')>=0) return '用多个像素点在屏幕上拼出笑脸图案，每个像素就是一个小格子。';
      return '在屏幕上点亮一个像素点，像素是屏幕最小的发光格子。';
    }
    if(n.indexOf('显示')>=0){
      if(n.indexOf('数字')>=0) return '在屏幕上显示一个数字，数字会更新覆盖之前的内容。';
      if(n.indexOf('变量')>=0) return '把变量里存的数字取出来显示在屏幕上，变量变了显示也跟着变。';
      if(n.indexOf('文字')>=0) return '在屏幕上显示一行文字，是CyberPi跟人"说话"的主要方式。';
      return '在屏幕上显示指定内容（文字、数字或变量值）。';
    }
    return '控制屏幕显示内容。';
  }
  if(cat==='灯'){
    if(n.indexOf('熄灭')>=0 && n.indexOf('亮起')>=0) return '切换RGB灯的亮灭状态，让灯在亮和灭之间来回切换。';
    if(n.indexOf('熄灭')>=0) return '把RGB灯关掉，灯不发光。';
    if(n.indexOf('亮起')>=0){
      if(n.indexOf('红=')>=0||n.indexOf('绿=')>=0||n.indexOf('蓝=')>=0) return '按红绿蓝三个通道亮度值(0-255)混合出颜色，三种光配比不同颜色就不同。';
      var cs=[]; ['红色','绿色','蓝色','黄色'].forEach(function(c){ if(n.indexOf(c)>=0) cs.push(c); });
      if(cs.length) return '把RGB灯调成'+cs.join('、')+'，灯立刻亮起该颜色。';
      return '把RGB灯调成指定颜色并亮起。';
    }
    return '控制5颗RGB彩灯的颜色和亮灭。';
  }
  if(cat==='声音'){
    if(n.indexOf('朗读')>=0) return '把文字变成说话声读出来（语音合成），是AI的"嘴巴"，需要联网。';
    if(n.indexOf('播放音符')>=0) return '播放指定音高和时长的音符，可以拼成简单旋律。';
    if(n.indexOf('播放')>=0){
      if(n.indexOf('提示')>=0) return '播放一段短促提示音，提醒用户"操作成功了"。';
      if(n.indexOf('奖励')>=0) return '播放一段欢快奖励音效，做对了给点听觉鼓励。';
      return '播放指定的音效或声音。';
    }
    return '控制扬声器播放声音。';
  }
  if(cat==='传感'){
    if(n.indexOf('环境光')>=0) return '读取当前环境光线亮暗程度，返回0-100的数字，越亮数字越大。';
    if(n.indexOf('声音强度')>=0||n.indexOf('音量')>=0) return '读取麦克风检测到的声音大小，声音越大数字越大。';
    if(n.indexOf('加速度')>=0||n.indexOf('摇一摇')>=0||n.indexOf('陀螺仪')>=0){
      if(n.indexOf('X')>=0||n.indexOf('x')>=0) return '读取X轴加速度，左右倾斜时数值变化，向左摇为负、向右摇为正。';
      return '读取加速度传感器数值，感知摇晃、倾斜和移动方向。';
    }
    if(n.indexOf('按钮')>=0) return '检测按钮是否被按下，返回真/假，判断用户有没有操作。';
    return '读取传感器检测到的外界信息。';
  }
  if(cat==='运算'){
    if(n.indexOf('随机数')>=0){ var m3=n.match(/(\\d+)[-~到](\\d+)/); return '随机生成一个'+(m3?m3[1]+'到'+m3[2]:'指定范围')+'之间的整数，每次结果可能不同。'; }
    if(n.indexOf('增加')>=0) return '把变量的值加上指定数量，比如加1就是每次多1，常用于计数。';
    if(n.indexOf('总和')>=0||n.indexOf('÷')>=0) return '做除法运算，把总和除以份数得到平均值。';
    if(n.indexOf('且')>=0||n.indexOf('与')>=0) return '逻辑"与"：两个条件都满足时结果才为真，缺一不可。';
    if(n.indexOf('比较')>=0||n.indexOf('>')>=0||n.indexOf('<')>=0||n.indexOf('=')>=0) return '比较两个值的大小或是否相等，结果为真或假，用于条件判断。';
    if(n.indexOf('综合分')>=0||n.indexOf('×')>=0||n.indexOf('+')>=0) return '加权求和：每个输入乘以它的权重（重要程度），再加起来得到综合分。';
    return '做数学计算和逻辑运算。';
  }
  if(cat==='变量'){
    if(n.indexOf('建立变量')>=0) return '创建一个有名字的"小抽屉"，存数字或文字，程序运行中可随时取用和修改。';
    if(n.indexOf('记录')>=0) return '把当前读到的传感器数值存进变量，留着后面计算用。';
    if(n.indexOf('组')>=0&&n.indexOf('+1')>=0) return '对应分组的计数器加1，每检测到一次该组就记一笔。';
    return '创建和使用变量存储数据。';
  }
  if(cat==='自制'){
    if(n.indexOf('定义')>=0) return '把一串积木打包成一个新的自定义积木，起个好记的名字，以后直接调用就能执行整串步骤。';
    return '定义和调用自制积木。';
  }
  if(cat==='扩展'){
    if(n.indexOf('训练')>=0){
      if(n.indexOf('只训练')>=0) return '只采集指定类别样本训练（故意只练一类），用来演示数据偏见的问题。';
      if(n.indexOf('声音类别')>=0) return '采集一类声音样本作为训练数据，让机器学习认识这种声音。';
      return '采集样本数据训练机器学习模型。';
    }
    if(n.indexOf('识别')>=0) return '用训练好的模型识别当前声音属于哪个类别，返回识别结果标签。';
    if(n.indexOf('补训练')>=0) return '补充采集之前缺少的类别样本重新训练，让模型学得更全面。';
    return '机器学习扩展功能。';
  }
  if(cat==='网络/AI'){
    if(n.indexOf('识别语音')>=0) return '录一段音发送到云端识别成文字（语音转文字），需要联网。';
    if(n.indexOf('语音识别结果')>=0) return '取出上一次语音识别得到的文字结果，用来做后续判断。';
    return 'AI语音识别功能。';
  }
  return '一个编程积木。';
}
function panelBlocks(l, ch){
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

if old_panel in src:
    src = src.replace(old_panel, new_panel, 1)
    print("OK: replaced panelBlocks function")
else:
    print("FAIL: old_panel not found")
    # debug
    idx = src.find("面板：编程积木")
    if idx >= 0:
        print("context:", repr(src[idx:idx+200]))

# === 添加新CSS样式 ===
old_css_marker = """.blk-row{display:flex;gap:12px;align-items:center;margin-bottom:10px}
.blk-lab{font-size:11px;font-weight:800;color:#fff;padding:3px 10px;border-radius:8px;letter-spacing:.5px;flex:none}
.blk{color:#fff;font-size:13.5px;font-weight:700;padding:8px 16px;border-radius:10px;display:inline-flex;align-items:center;gap:8px;box-shadow:0 3px 10px -4px rgba(0,0,0,.25)}
.blk-cat{font-size:10px;opacity:.75;font-weight:800;letter-spacing:.5px}
.blk-list{margin-top:14px}"""

new_css = """.blk-guide{display:flex;gap:16px;align-items:flex-start;background:linear-gradient(135deg,hsl(214 80% 97%),hsl(28 100% 97%));border:2px solid hsl(214 60% 88%);border-radius:16px;padding:18px 20px;margin-bottom:18px}
.blk-guide .bg-ico{width:44px;height:44px;border-radius:12px;background:var(--primary);color:#fff;display:grid;place-items:center;flex:none}
.blk-guide .bg-ico svg{width:24px;height:24px}
.blk-guide b{font-size:15px;color:var(--ink);display:block;margin-bottom:4px}
.blk-guide p{font-size:13px;color:var(--ink-2);line-height:1.7;margin:0}
.blk-cat-intro{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin-bottom:18px}
.bci-item{display:flex;gap:10px;align-items:flex-start;background:var(--accent);border-radius:12px;padding:12px 14px}
.bci-dot{width:12px;height:12px;border-radius:4px;flex:none;margin-top:3px}
.bci-item b{font-size:13px;color:var(--ink);display:block;margin-bottom:2px}
.bci-item p{font-size:11.5px;color:var(--ink-2);line-height:1.6;margin:0}
.blk-cards{display:flex;flex-direction:column;gap:12px;margin-bottom:14px}
.blk-card{background:#fff;border:1.5px solid var(--line);border-radius:14px;padding:14px 16px;box-shadow:var(--shadow-sm)}
.blk-card-top{display:flex;gap:12px;align-items:center;margin-bottom:10px;flex-wrap:wrap}
.blk-desc{font-size:13px;color:var(--ink-2);line-height:1.7;padding-left:4px;border-left:3px solid var(--primary-100);padding-top:4px;padding-bottom:4px}
.blk-row{display:flex;gap:12px;align-items:center;margin-bottom:10px}
.blk-lab{font-size:11px;font-weight:800;color:#fff;padding:3px 10px;border-radius:8px;letter-spacing:.5px;flex:none}
.blk{color:#fff;font-size:13.5px;font-weight:700;padding:8px 16px;border-radius:10px;display:inline-flex;align-items:center;gap:8px;box-shadow:0 3px 10px -4px rgba(0,0,0,.25)}
.blk-cat{font-size:10px;opacity:.75;font-weight:800;letter-spacing:.5px}
.blk-list{margin-top:14px}"""

if old_css_marker in src:
    src = src.replace(old_css_marker, new_css, 1)
    print("OK: added new CSS styles")
else:
    print("FAIL: old_css_marker not found")
    idx = src.find(".blk-row")
    if idx >= 0:
        print("context:", repr(src[idx:idx+150]))

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(src)
print("DONE: file saved")
