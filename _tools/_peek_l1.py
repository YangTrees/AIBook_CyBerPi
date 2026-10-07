# -*- coding: utf-8 -*-
"""查看 LESSONS_1 第一条完整数据 + CURRICULUM_REFINEMENTS 第一条 + sampleOf/sample数据"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

i = s.find('var LESSONS_1')
print('LESSONS_1 at', i)
print(s[i:i+2400])
