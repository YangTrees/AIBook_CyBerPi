# -*- coding: utf-8 -*-
"""提取现有32课 id/title/theme/blocks关键词"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

# 提取所有课程对象：id/title/theme
pat = re.compile(r'id:(\d+),\s*ch:\d+,\s*title:"([^"]+)",\s*theme:"([^"]+)"')
rows = pat.findall(s)
print('课程数:', len(rows))
for rid, title, theme in rows:
    print(f'L{rid:>2} | {title} | {theme}')
