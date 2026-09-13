# -*- coding: utf-8 -*-
import io, re
p = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts\app.js"
s = io.open(p, encoding="utf-8").read()
# 修复 esc 函数中正则里的引号（被误转为中文引号）
s = s.replace('replace(/"/g,\u201c&quot;\")', 'replace(/"/g,"&quot;")')
s = s.replace('replace(/"/g,\u201c&quot;\")', 'replace(/"/g,"&quot;")')
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
# 检查是否还有其他正则含中文引号
for m in re.finditer(r"/.{0,40}/[a-z]*", s):
    seg = m.group(0)
    if "\u201c" in seg or "\u201d" in seg:
        print("regex with cn quote:", seg)
print("esc line:", [l for l in s.split("\n") if "&quot;" in l][0])
