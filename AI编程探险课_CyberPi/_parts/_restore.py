# -*- coding: utf-8 -*-
import io
parts = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts"
path = parts + "\\app.js"
s = io.open(path, encoding="utf-8").read()
# 恢复被误转的连接字符串边界引号：+ 两侧的中文引号还原为 ASCII 双引号
before = s
s = s.replace("\u201c+", '" +').replace("+\u201d", '+"').replace("+\u201c", '+"').replace("\u201d+", '" +')
# 兼容无空格拼接（原文件为 "+ 或 +"，此处还原为 "+ 或 +"）
s = s.replace('\u201c+', '"+').replace('+\u201d', '+"')
io.open(path, "w", encoding="utf-8", newline="\n").write(s)
print("restored chars:", sum(1 for a,b in zip(before, s) if a != b))
