# -*- coding: utf-8 -*-
# 通用引号修复：跟踪单/双引号字符串状态，将双引号字符串内部的 ASCII " 转为中文引号
import io

STRUCT = set(",]});:")

def fix_line(line):
    out = []
    state = None       # None / ' / "
    inner_open = False
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == "\\":
            out.append(ch)
            if i + 1 < n:
                out.append(line[i+1])
                i += 2
                continue
            i += 1
            continue
        if ch == "'":
            if state is None:
                state = "'"
                out.append(ch)
            elif state == "'":
                state = None
                out.append(ch)
            else:  # 双引号字符串内的单引号是字面量
                out.append(ch)
        elif ch == '"':
            if state is None:
                state = '"'
                inner_open = True
                out.append(ch)
            elif state == '"':
                j = i + 1
                while j < n and line[j] == " ":
                    j += 1
                nxt = line[j] if j < n else ""
                if nxt == "" or nxt in STRUCT:
                    state = None
                    out.append(ch)
                else:
                    out.append("\u201c" if inner_open else "\u201d")
                    inner_open = not inner_open
            else:  # 单引号字符串内的双引号是字面量
                out.append(ch)
        else:
            out.append(ch)
        i += 1
    return "".join(out), state

parts = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts"
path = parts + "\\app.js"
lines = io.open(path, encoding="utf-8").read().split("\n")
fixed, stray = [], 0
for ln in lines:
    new, dangling = fix_line(ln)
    fixed.append(new)
    if dangling:
        stray += 1
io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(fixed))
print("app.js fixed; lines with dangling quote:", stray)
