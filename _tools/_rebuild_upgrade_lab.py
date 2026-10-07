# -*- coding: utf-8 -*-
"""重写「试玩与升级」模块：PLAY LAB -> UPGRADE LAB（调一调/换一换/记一记）"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

new_fn = '''function paramExperiments(l){
  var exps = [], seen = {};
  var colorPairs = {红:'紫',绿:'蓝',蓝:'青',黄:'白',紫:'红',白:'绿',青:'粉',粉:'黄',橙:'蓝',黄绿:'粉'};
  l.blocks.forEach(function(b){
    var name = b[1];
    if(!name || seen[name]) return;
    seen[name] = 1;
    var m;
    m = name.match(/等待([\\d.]+)秒/);
    if(m){
      var n = parseFloat(m[1]);
      var fast = Math.max(0.1, Math.round(n/2*10)/10);
      var slow = Math.round(n*2*10)/10;
      exps.push(['试试节奏','把「'+name+'」改成「等待'+slow+'秒」或「等待'+fast+'秒」','看看灯光/动作是变慢还是变快']);
      return;
    }
    m = name.match(/RGB灯亮起\\s*(.+)/);
    if(m){
      var c = m[1], alt = colorPairs[c] || '蓝色';
      exps.push(['试试颜色','把「RGB灯亮起 '+c+'」改成「RGB灯亮起 '+alt+'」','换一种颜色，看看搭配效果']);
      return;
    }
    m = name.match(/显示(标签|文字)「(.+)」/);
    if(m){
      var t = m[2], alt2 = t.length > 2 ? t.slice(0,2)+'～' : '你好呀';
      exps.push(['试试文字','把「显示'+m[1]+'」里的「'+t+'」改成「'+alt2+'」','屏幕上的内容变个样']);
      return;
    }
    m = name.match(/(\\d+)/);
    if(m){
      var d = parseInt(m[1],10), d2 = Math.min(10, d+1);
      exps.push(['试试数字','把「'+name+'」里的数字 '+d+' 改成 '+d2,'数值一变，反应就不同']);
    }
  });
  if(exps.length > 2) exps = exps.slice(0,2);
  return exps;
}
function lessonOutputs(l){
  var outs = [];
  l.blocks.forEach(function(b){
    var cat = b[0];
    if((cat==='显示'||cat==='灯'||cat==='声音'||cat==='外观') && outs.indexOf(cat)===-1) outs.push(cat);
  });
  return outs.length ? outs.join('、') : '屏幕、灯光或声音';
}
function sampleTestLab(l){
  var exps = paramExperiments(l);
  var outputs = lessonOutputs(l);
  var wrenchIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 6.5a4.5 4.5 0 1 0-5.8 6.2L3 18.5V21h2.5l5.8-5.7a4.5 4.5 0 0 0 6.2-5.8l-3 3-2.6-.6-.6-2.6 3-3z"/></svg>';
  var starIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 2.7 5.5 6 .9-4.3 4.2 1 6-5.4-2.8L6.6 19.6l1-6L3.3 9.4l6-.9L12 3z"/></svg>';
  var penIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.8 2.8 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/></svg>';
  var expCases = exps.length ? exps.map(function(r,i){
    return '<div class="play-case"><span>'+esc(r[0])+'</span><b>'+esc(r[1])+'</b><i>动手做</i><p>'+esc(r[2])+'</p></div>';
  }).join('') : '<div class="play-case"><span>试试</span><b>找出程序里的一个数字或颜色</b><i>动手做</i><p>把它改一改，再运行一次，看看 CyberPi 有什么不同。</p></div>';
  return '<section class="sample-test-lab kid-test-lab"><div class="sample-test-head"><div><span>UPGRADE LAB · 实验升级站</span><h4>调一调，换一换，记一记</h4></div><p>作品完成后，来当一回小小发明家：每次只改一处，马上在 CyberPi 上验证。</p></div><div class="kid-test-route">'+
    '<article class="kid-test-card try-card"><header><i>'+wrenchIcon+'</i><div><small>实验 1</small><b>调一调参数</b></div></header><p class="card-lead">本课程序里的数字、颜色和文字，都可以拿来玩。</p><div class="play-cases">'+expCases+'</div></article>'+
    '<article class="kid-test-card upgrade-card"><header><i>'+starIcon+'</i><div><small>实验 2</small><b>换一换玩法</b></div></header><p class="card-lead">完成作品后，再挑战一个更有趣的升级任务。</p><div class="upgrade-action"><span>本课挑战</span><p>'+esc(l.challenge || '试着换一种输入或输出，说说程序逻辑有什么变化。')+'</p></div><div class="upgrade-action"><span>说一说</span><p>你改了哪里？CyberPi 的回应有什么不同？</p></div></article>'+
    '<article class="kid-test-card find-card"><header><i>'+penIcon+'</i><div><small>实验 3</small><b>记一记发现</b></div></header><p class="card-lead">每次改动后，把看到的记下来，你就真的学会啦。</p><div class="bug-clues">'+
      '<div class="bug-clue"><b>改动前后，CyberPi 的'+outputs+'发生了什么变化？</b><p>用一句话说出来，比如：“我把等待改成 2 秒，所以灯停得更久了。”</p></div>'+
      '<div class="bug-clue"><b>把发现说给团团或点点听</b><p>能说出“我改了 X，所以 Y”，本课的发明家挑战就成功啦。</p></div>'+
    '</div></article>'+
  '</div></section>';
}
'''

# 定位并替换 sampleTestLab 函数（含前导的 sampleTaskLab 之后）
start = s.find('function sampleTestLab')
assert start != -1, 'sampleTestLab 未找到'
end = s.find('function panelChallenge', start)
assert end != -1, 'panelChallenge 未找到'
# 确保替换范围正确：找到 sampleTestLab 函数结束（下一个顶层 function）
nxt = s.find('\nfunction ', start + 20)
assert nxt != -1 and nxt < end, (nxt, end)
old_block = s[start:nxt]
print('旧函数长度:', len(old_block))
s2 = s[:start] + new_fn + s[nxt:]

# 更新 panelChallenge 标题与说明
old_title = '<h3><span class="t-ico" style="background:\'+ch.color+\'">\'+TABS[4].icon+\'</span>试玩、找错和升级</h3>'
new_title = '<h3><span class="t-ico" style="background:\'+ch.color+\'">\'+TABS[4].icon+\'</span>实验升级站</h3>'
assert s2.count(old_title) == 1, s2.count(old_title)
s2 = s2.replace(old_title, new_title)

old_box = '<div class="challenge-box"><span class="c-tag">团团和点点的试玩站</span><p>让 CyberPi 跑起来，多试几种玩法。没成功也没关系：看一看、改一处，再试一次。</p></div>'
new_box = '<div class="challenge-box"><span class="c-tag">团团和点点的实验站</span><p>让 CyberPi 跑起来，多试几种玩法。每次只改一处，看一看、改一改，再试一次。</p></div>'
assert s2.count(old_box) == 1, s2.count(old_box)
s2 = s2.replace(old_box, new_box)

io.open(p, 'w', encoding='utf-8', newline='').write(s2)
import re
print('paramExperiments 定义:', s2.count('function paramExperiments'))
print('UPGRADE LAB:', s2.count('UPGRADE LAB · 实验升级站'))
print('剩余 PLAY LAB:', s2.count('PLAY LAB'))
print('完成')
