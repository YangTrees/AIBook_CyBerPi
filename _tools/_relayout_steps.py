# -*- coding: utf-8 -*-
"""布局调整 v2：直接从文件读取原文构造 anchor，动图独立全宽卡 + 文字步骤竖排"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

# 用正则匹配整个 step-shot 渲染块（从 step-shot-head 到 join('')+'</div></section>';）
pat = re.compile(r"    '<div class=\"step-shot-head\"><b>关键步骤</b>.*?join\(''\)\+'</div></section>';", re.S)
m = pat.search(s)
assert m, 'pattern not found'
old = m.group(0)
print('anchor len:', len(old))

new = """    '<div class="step-shot-head"><b>关键步骤</b><span>'+(OFFICIAL_STEPS[l.id]?'官方搭建动画 + 文字步骤':'第 2\u20134 步已配图，点击可放大')+'</span></div>'+((OFFICIAL_STEPS[l.id])?
      '<figure class="official-step-card zoomable-shot" onclick="openImgLightbox(\\''+OFFICIAL_STEPS[l.id]+'\\',\\''+esc(l.title)+' 搭建动画\\')"><img src="'+OFFICIAL_STEPS[l.id]+'" alt="'+esc(l.title)+' 搭建动画"><span class="zoom-badge">点击放大</span></figure>'+
      '<div class="step-list">'+stepTitles.map(function(n,i){
        var last = (i === stepTitles.length-1);
        return '<div class="step-row"><i>'+((i+1)<10?'0':'')+(i+1)+'</i><div><b>'+esc(n)+'</b><small>'+((i===0)?'先完成设备与变量准备':(last?'在 CyberPi 真机完成验收':'按文字说明完成本步搭建'))+'</small></div><em>'+((i===0)?'准备':(last?'验收':'搭建'))+'</em></div>';
      }).join('')+'</div>'
    :
      '<div class="step-shot-grid">'+stepTitles.map(function(n,i){
        var shot = (i >= 1 && i <= 3) ? 'assets/blocks/lesson-'+pad+'/step-0'+(i+1)+'.png' : '';
        if(!shot) return '<div class="shot-slot"><span>0'+(i+1)+'</span><i>'+((i===0)?'准备':'验证')+'</i><b>'+esc(n)+'</b><small>'+((i===0)?'先完成设备与变量准备':'在 CyberPi 真机完成验收')+'</small></div>';
        return '<div class="shot-slot has-shot zoomable-shot" onclick="openImgLightbox(\\''+shot+'\\',\\''+esc(n)+'\\')"><span>0'+(i+1)+'</span><img src="'+shot+'" alt="'+esc(n)+'"><b>'+esc(n)+'</b><small>点击图片放大查看</small></div>';
      }).join('')+'</div>'
    )+'</section>';"""

s = s.replace(old, new)

# CSS 注入
css = """.official-step-card{position:relative;margin-bottom:14px;border-radius:18px;overflow:hidden;background:linear-gradient(160deg,#14141F,#20202F);box-shadow:5px 7px 14px rgba(76,58,106,.1)}
.official-step-card img{width:100%;aspect-ratio:3/2;object-fit:contain;display:block}
.step-list{display:grid;gap:9px}
.step-row{display:grid;grid-template-columns:34px minmax(0,1fr) auto;gap:12px;align-items:center;padding:11px 13px;border:1px solid rgba(255,255,255,.9);border-radius:15px;background:#FBF9FF;box-shadow:3px 4px 8px rgba(76,58,106,.05)}
.step-row>i{width:32px;height:32px;border-radius:10px;display:grid;place-items:center;background:#7C3AED;color:#fff;font-size:11px;font-weight:900;font-style:normal}
.step-row b{font-size:12px;line-height:1.5}
.step-row small{display:block;font-size:9.5px;color:#9B90A5;margin-top:2px}
.step-row em{font-size:9px;font-style:normal;font-weight:900;color:#7C3AED;background:#EDE9FE;padding:4px 7px;border-radius:8px}
"""
anchor_css = '.shot-slot{position:relative;min-height:152px;'
ai = s.find(anchor_css)
assert ai != -1, 'css anchor'
s = s[:ai] + css + s[ai:]

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK 布局调整完成')
