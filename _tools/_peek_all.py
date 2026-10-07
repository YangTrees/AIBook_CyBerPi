# -*- coding: utf-8 -*-
"""查看 ALL 数组结构(第一条) 与 CURRICULUM_REFINEMENTS(前几条)"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

i = s.find('var ALL')
print('ALL at', i)
print(s[i:i+3000])
