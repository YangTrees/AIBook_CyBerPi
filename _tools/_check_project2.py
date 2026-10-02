# -*- coding: utf-8 -*-
"""项目检查 v2：JS 字符串中的资源引用（单双引号/模板串），精确定位舞台角色问题课程"""
import io, os, re

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi'
HTML = os.path.join(ROOT, 'index.html')
s = io.open(HTML, encoding='utf-8').read()

# ---- 资源引用（JS 字符串内，单双引号皆可）----
refs = set(re.findall(r'''['"](assets/[^'"]+\.(?:png|jpg|jpeg|gif|webp|svg))['"]''', s))
refs |= set(re.findall(r'["\'](\.\./assets/[^"\']+\.(?:png|jpg|jpeg|gif|webp|svg))["\']', s))
missing = []
for r in sorted(refs):
    r2 = r.replace('../', '')
    parts = r2.split('/')
    full = os.path.join(ROOT, *parts)
    if not os.path.exists(full):
        missing.append(r)
print('=== 资源引用 ===')
print('引用(去重):', len(refs), ' 缺失:', len(missing))
for m in missing[:40]:
    print('  MISS:', m)
from collections import Counter
pref = Counter()
for r in refs:
    pref[r.split('/')[1]] += 1
print('按目录:', dict(pref))

# ---- 舞台/角色/广播 问题课程定位 ----
print('\n=== 舞台/角色/广播 问题 ===')
# 提取每个课程对象范围（找 "N:{meaning" 或课程数据）
lines = s.split('\n')
cur = None
for i, ln in enumerate(lines, 1):
    if re.search(r'^\s*\d+:\(\{meaning', ln) or re.search(r'^\s*\d+:\(', ln) and 'meaning' in ln:
        cur = ln.strip()[:60]
    if any(k in ln for k in ['舞台', '角色', '广播']):
        print('L%d [%s]' % (i, (cur or '?')[:40]))
        print('   ', ln.strip()[:150])
