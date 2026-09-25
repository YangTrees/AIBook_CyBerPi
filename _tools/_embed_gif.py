# -*- coding: utf-8 -*-
"""把官方动图嵌入 index.html：CSS + sampleMediaStudio 的 video-slot 替换"""
import io

P = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(P, encoding='utf-8').read()

# 1) CSS：在 .full-code-slot 规则后插入 .official-gif 规则
old_css = ".full-code-slot span{display:block;font-size:10px;color:var(--ink-2);margin-top:3px}"
new_css = old_css + "\n.official-gif{position:relative;min-height:250px;border:1px solid rgba(255,255,255,.9);border-radius:21px;overflow:hidden;background:#fff;box-shadow:5px 7px 14px rgba(76,58,106,.1);display:grid;grid-template-rows:minmax(0,1fr) auto}.official-gif img{width:100%;height:250px;object-fit:contain;padding:10px;background:linear-gradient(160deg,#14141F,#20202F)}.official-gif figcaption{padding:12px 14px;background:#fff}.official-gif b{display:block;font-size:13px}.official-gif span{display:block;font-size:10px;color:var(--ink-2);margin-top:3px}.official-gif .gif-badge{display:inline-block;margin-top:6px;padding:5px 8px;border-radius:9px;background:#F59E0B;color:#fff;font-size:9px;font-style:normal;font-weight:900}"
assert s.count(old_css) == 1, f'CSS锚点数量异常: {s.count(old_css)}'
s = s.replace(old_css, new_css)

# 2) JS：sampleMediaStudio 中 video-slot → official-gif 卡片
old_js = "'<div class=\"media-featured\"><div class=\"video-slot\" style=\"--poster:url(\\''+lessonAsset(l.id)+'\\')\"><div class=\"play-mark\">▶</div><b>最终效果视频</b><span>程序运行 + CyberPi 反馈 · 30–90 秒</span><em>待上传</em></div>'+"
new_js = "'<div class=\"media-featured\"><figure class=\"official-gif zoomable-shot\" onclick=\"openImgLightbox(\\'assets/yuque_web/lesson-'+pad+'.gif\\',\\'官方演示动图 - '+esc(l.title)+'\\')\"><img src=\"assets/yuque_web/lesson-'+pad+'.gif\" alt=\"官方演示动图 - '+esc(l.title)+'\"><span class=\"zoom-badge\">点击放大</span><figcaption><b>官方演示动图</b><span>语雀官方课程效果演示 · 点击放大</span><em class=\"gif-badge\">动图</em></figcaption></figure>'+"
assert s.count(old_js) == 1, f'JS锚点数量异常: {s.count(old_js)}'
s = s.replace(old_js, new_js)

io.open(P, 'w', encoding='utf-8').write(s)
print('OK 已嵌入官方动图')
