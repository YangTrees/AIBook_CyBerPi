# -*- coding: utf-8 -*-
"""清理响应式媒体查询中的 workflow 残留"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

subs = [
    '  .workflow-grid{grid-template-columns:repeat(2,1fr)}\n',
    '.workflow-head{align-items:flex-start;flex-direction:column}.workflow-head p{text-align:left}.workflow-grid{grid-template-columns:1fr}',
]
for sub in subs:
    c = s.count(sub)
    assert c == 1, (sub[:30], c)
    s = s.replace(sub, '')
    print('已删除:', sub[:60])

io.open(p, 'w', encoding='utf-8', newline='').write(s)
import re
print('剩余 workflow 引用:', len(re.findall(r'workflow', s)))
