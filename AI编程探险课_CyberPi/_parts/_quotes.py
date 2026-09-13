# -*- coding: utf-8 -*-
# 将数据文件中字符串内部的中文引号（ASCII "）转换为中文引号 “ ”
import io

parts = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts"
targets = ["data1.js", "data2.js", "data3.js", "data4.js"]
STRUCT = set(",]});:")

def fix_line(line):
    out = []
    in_str = False
    inner_open = False  # 当前字符串内下一对内部引号是否为左引号
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == '"':
            if not in_str:
                in_str = True
                inner_open = True
                out.append(ch)
            else:
                # 向后看下一个非空格字符
                j = i + 1
                while j < n and line[j] == " ":
                    j += 1
                nxt = line[j] if j < n else ""
                if nxt == "" or nxt in STRUCT:
                    in_str = False
                    out.append(ch)
                else:
                    out.append("\u201c" if inner_open else "\u201d")
                    inner_open = not inner_open
        else:
            out.append(ch)
        i += 1
    return "".join(out), in_str

for fn in targets:
    path = parts + "\\" + fn
    lines = io.open(path, encoding="utf-8").read().split("\n")
    fixed, stray = [], 0
    for ln in lines:
        new, dangling = fix_line(ln)
        fixed.append(new)
        if dangling:
            stray += 1
    io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(fixed))
    print(fn, "fixed; lines with dangling quote:", stray)
