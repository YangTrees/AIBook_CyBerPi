# -*- coding: utf-8 -*-
"""删除 .platform-workflow 系列CSS"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

# 构造从 .platform-workflow{ 到 .workflow-grid p{...} 结束的完整规则串
pat = re.compile(r'\.platform-workflow\{.*?\.workflow-grid p\{[^}]*\}', re.S)
m = pat.search(s)
assert m, 'CSS块未找到'
css = m.group(0)
print('CSS块长度:', len(css), '开头:', css[:40], '结尾:', css[-60:])
s2 = s[:m.start()] + s[m.end():]
io.open(p, 'w', encoding='utf-8', newline='').write(s2)
left = len(re.findall(r'\.platform-workflow|\.workflow-head|\.workflow-grid', s2))
print('剩余 workflow CSS 引用:', left)
