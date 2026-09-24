# -*- coding: utf-8 -*-
"""验证 index.html 数据完整性：LESSONS、CHAPTERS、CURRICULUM_REFINEMENTS、SAMPLE_CONTENT"""
import re, json, os

p = r'D:\AI\_AIBook\AIBook_Offline_CyberPi\AI编程探险课_CyberPi\index.html'
s = open(p, encoding='utf-8').read()

# 1. LESSONS 数量
counts = []
for i in range(1, 5):
    m = re.search(rf'const LESSONS_{i} = \[(.*?)\];', s, re.DOTALL)
    if m:
        n = m.group(1).count('id:')
        counts.append(n)
print('LESSONS 数量:', counts, '总:', sum(counts))

# 2. CHAPTERS
m = re.search(r'var CHAPTERS = \[(.*?)\];', s, re.DOTALL)
if m:
    names = re.findall(r"name:'([^']+)'", m.group(1))
    print('CHAPTERS:', names)

# 3. CURRICULUM_REFINEMENTS 条数
m = re.search(r'const CURRICULUM_REFINEMENTS = \{(.*?)\};', s, re.DOTALL)
if m:
    n = len(re.findall(r'meaning:"', m.group(1)))
    print('REFINEMENTS 条数:', n)

# 4. SAMPLE_CONTENT 条数
m = re.search(r'var SAMPLE_CONTENT = \{(.*?)\};', s, re.DOTALL)
if m:
    n = len(re.findall(r'stepShots:', m.group(1)))
    print('SAMPLE_CONTENT 条数:', n)

# 5. 抽查第一课 title
m = re.search(r'id:1, ch:1, title:"([^"]+)"', s)
print('第1课title:', m.group(1) if m else '未找到')

m = re.search(r'id:32, ch:4, title:"([^"]+)"', s)
print('第32课title:', m.group(1) if m else '未找到')

# 6. 首页文案检查
checks = [
    ('brand', 'CyberPi 积木编程探险课'),
    ('hero', '像搭积木一样学会编程'),
    ('ch1', '第一章 初识CyberPi'),
    ('chip', '编程能力递进 · 32 课'),
]
for name, key in checks:
    print(f'{name}: {"✓" if key in s else "✗ 未找到: " + key}')
