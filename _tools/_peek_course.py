# -*- coding: utf-8 -*-
"""查看 COURSE 数据一条样例结构 + sampleTestLab 调用位置"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

i = s.find('COURSE = ')
if i == -1:
    i = s.find('var COURSE')
print('COURSE at', i)
print(s[i:i+2600])
