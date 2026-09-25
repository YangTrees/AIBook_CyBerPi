# -*- coding: utf-8 -*-
"""1) 注入 OFFICIAL_STEPS 映射  2) step渲染优先官方图  3) 新增CSS"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

# ---- 1) OFFICIAL_STEPS 映射（插入到 CURRICULUM_REFINEMENTS 定义之后）----
maps = {
    1:'gif',2:'gif',3:'gif',4:'gif',5:'gif',6:'gif',7:'gif',8:'gif',9:'gif',10:'gif',
    11:'gif',12:'gif',13:'gif',14:'gif',15:'gif',16:'gif',17:'gif',18:'gif',19:'gif',20:'gif',
    21:'png',22:'gif',25:'gif',28:'gif',29:'gif'
}
lines = ['var OFFICIAL_STEPS = {']
for lid in sorted(maps):
    lines.append(f"  {lid}: 'assets/yuque_steps/lesson-{lid:02d}/step-02.{maps[lid]}',")
lines.append('};')

anchor = 'var CAT_COLOR = {'
ai = s.find(anchor)
assert ai != -1
s2 = s[:ai] + '\n'.join(lines) + '\n\n' + s[ai:]

# ---- 2) 修改 step-shot 渲染：step-02 优先官方图 ----
old_render = """var shot = (i >= 1 && i <= 3) ? 'assets/blocks/lesson-'+pad+'/step-0'+(i+1)+'.png' : '';
      return shot ? '<div class="shot-slot has-shot zoomable-shot" onclick="openImgLightbox(\\''+shot+'\\',\\''+esc(n)+'\\')"><span>0'+(i+1)+'</span><img src="'+shot+'" alt="'+esc(n)+'"><b>'+esc(n)+'</b><small>点击图片放大查看</small></div>' : '<div class="shot-slot"><span>0'+(i+1)+'</span><i>'+((i===0)?'准备':'验证')+'</i><b>'+esc(n)+'</b><small>'+((i===0)?'先完成设备与变量准备':'在 CyberPi 真机完成验收')+'</small></div>';"""
new_render = """var off = (i === 1) ? (OFFICIAL_STEPS[l.id] || '') : '';
      var shot = off || ((i >= 1 && i <= 3) ? 'assets/blocks/lesson-'+pad+'/step-0'+(i+1)+'.png' : '');
      if(!shot) return '<div class="shot-slot"><span>0'+(i+1)+'</span><i>'+((i===0)?'准备':'验证')+'</i><b>'+esc(n)+'</b><small>'+((i===0)?'先完成设备与变量准备':'在 CyberPi 真机完成验收')+'</small></div>';
      var isGif = off.slice(-4) === '.gif';
      return '<div class="shot-slot has-shot zoomable-shot'+(off?' official-step':'')+'" onclick="openImgLightbox(\\''+shot+'\\',\\''+esc(n)+'\\')"><span>0'+(i+1)+'</span><img src="'+shot+'" alt="'+esc(n)+'"><b>'+esc(n)+'</b><small>'+(off?(isGif?'官方步骤动画 · 点击放大':'官方步骤图 · 点击放大'):'点击图片放大查看')+'</small></div>';"""
assert s2.count(old_render) == 1, s2.count(old_render)
s2 = s2.replace(old_render, new_render)

# ---- 3) 新增 CSS（插到 .shot-slot 相关样式附近）----
css = """/* 官方步骤动图 */
.shot-slot.official-step{background:linear-gradient(160deg,#20242e,#2e3440);border-color:rgba(255,255,255,.14);position:relative}
.shot-slot.official-step img{aspect-ratio:16/9;object-fit:cover}
.shot-slot.official-step>span{background:rgba(255,255,255,.16);color:#fff}
.shot-slot.official-step b{color:#fff}
.shot-slot.official-step small{color:rgba(255,255,255,.62)}
.shot-slot.official-step::after{content:"动画演示";position:absolute;top:9px;right:9px;padding:3px 8px;border-radius:99px;background:rgba(255,255,255,.92);color:#20242e;font-size:8px;font-weight:900}
"""
# 找 .step-shot-grid 样式行插入
sg = s2.find('.step-shot-grid')
assert sg != -1
# 在该规则结束(下一个 } 之后)插入
close = s2.find('}', sg)
s2 = s2[:close+1] + '\n' + css + s2[close+1:]

io.open(p, 'w', encoding='utf-8', newline='').write(s2)
import re
print('OFFICIAL_STEPS 注入:', s2.count('var OFFICIAL_STEPS'))
print('官方步骤渲染:', s2.count('official-step'))
print('完成')
