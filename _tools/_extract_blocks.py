# -*- coding: utf-8 -*-
"""Extract per-lesson blocks definitions from index.html LESSONS array."""
import re, json

p = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
html = open(p, encoding='utf-8').read()

# LESSONS array starts with [{ id:1 ...} ... { id:32 ...}]
# Find all lesson objects: match from {  id:(\d+) to the closing \n},
pat = re.compile(r'\{\s*\n\s*id:(\d+),(.*?)\n\}', re.S)
lessons = {}
for m in pat.finditer(html):
    lid = int(m.group(1))
    body = m.group(2)
    if lid < 1 or lid > 32:
        continue
    title = re.search(r'title:"([^"]*)"', body)
    blocks = re.search(r'blocks:\[(.*?)\],', body, re.S)
    proj = re.search(r'projName:"([^"]*)"', body)
    lessons[lid] = {
        'title': title.group(1) if title else '?',
        'projName': proj.group(1) if proj else '?',
        'blocks': blocks.group(1)[:400] if blocks else '?'
    }

for i in sorted(lessons):
    l = lessons[i]
    print(f"L{i:02d} {l['title']} / {l['projName']}")
    print("   blocks:", l['blocks'][:300].replace('\n', ' '))
