# -*- coding: utf-8 -*-
"""方案B：有官方步骤动图的课，第3/4步静态截图改为纯文字步骤卡，仅第2步保留官方动图"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

old = """    '<div class="step-shot-head"><b>关键步骤截图</b><span>第 2\u20134 步已配图，点击可放大</span></div><div class="step-shot-grid">'+stepTitles.map(function(n,i){
      var off = (i === 1) ? (OFFICIAL_STEPS[l.id] || '') : '';
      var shot = off || ((i >= 1 && i <= 3) ? 'assets/blocks/lesson-'+pad+'/step-0'+(i+1)+'.png' : '');
      if(!shot) return '<div class="shot-slot"><span>0'+(i+1)+'</span><i>'+((i===0)?'准备':'验证')+'</i><b>'+esc(n)+'</b><small>'+((i===0)?'先完成设备与变量准备':'在 CyberPi 真机完成验收')+'</small></div>';
      var isGif = off.slice(-4) === '.gif';
      return '<div class="shot-slot has-shot zoomable-shot'+(off?' official-step':'')+'" onclick="openImgLightbox(\\''+shot+'\\',\\''+esc(n)+'\\')"><span>0'+(i+1)+'</span><img src="'+shot+'" alt="'+esc(n)+'"><b>'+esc(n)+'</b><small>'+(off?(isGif?'官方步骤动画 · 点击放大':'官方步骤图 · 点击放大'):'点击图片放大查看')+'</small></div>';
    }).join('')+'</div></section>';"""

new = """    '<div class="step-shot-head"><b>关键步骤</b><span>'+((OFFICIAL_STEPS[l.id])?'第2步官方动画 · 其余为文字步骤':'第 2\u20134 步已配图，点击可放大')+'</span></div><div class="step-shot-grid">'+stepTitles.map(function(n,i){
      var off = (i === 1) ? (OFFICIAL_STEPS[l.id] || '') : '';
      var hasOfficial = !!OFFICIAL_STEPS[l.id];
      var shot = '';
      if(off) shot = off;
      else if(!hasOfficial && i >= 1 && i <= 3) shot = 'assets/blocks/lesson-'+pad+'/step-0'+(i+1)+'.png';
      if(!shot) return '<div class="shot-slot"><span>0'+(i+1)+'</span><i>'+((i===0)?'准备':(i===4?'验证':'搭建'))+'</i><b>'+esc(n)+'</b><small>'+((i===0)?'先完成设备与变量准备':(i===4?'在 CyberPi 真机完成验收':'按文字说明完成本步搭建'))+'</small></div>';
      var isGif = off.slice(-4) === '.gif';
      return '<div class="shot-slot has-shot zoomable-shot'+(off?' official-step':'')+'" onclick="openImgLightbox(\\''+shot+'\\',\\''+esc(n)+'\\')"><span>0'+(i+1)+'</span><img src="'+shot+'" alt="'+esc(n)+'"><b>'+esc(n)+'</b><small>'+(off?(isGif?'官方步骤动画 · 点击放大':'官方步骤图 · 点击放大'):'点击图片放大查看')+'</small></div>';
    }).join('')+'</div></section>';"""

assert s.count(old) == 1, 'anchor not found: %d' % s.count(old)
s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK 方案B替换完成')
