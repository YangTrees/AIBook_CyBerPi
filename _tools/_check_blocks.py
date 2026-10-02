# -*- coding: utf-8 -*-
"""提取所有课程 blocks 使用的分类集合 + 第10课内容"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

cats = set()
# blocks 数组模式: blocks:[[ "分类","积木名"],...]
for m in re.finditer(r'blocks:\[(\[\[[^\]]+\]\])\]', s):
    inner = m.group(1)
    for cm in re.finditer(r'\["([^"]+)","([^"]+)"\]', inner):
        cats.add(cm.group(1))
print('所有 blocks 分类:', sorted(cats))

# 第10课对象定位（id:10）
lines = s.split('\n')
start = None
for i, ln in enumerate(lines):
    if re.search(r'\bid:10\b', ln) and 'title' in ln:
        start = i
        break
if start:
    for ln in lines[start:start+14]:
        print(ln.strip()[:170])
