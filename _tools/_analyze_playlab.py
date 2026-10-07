# -*- coding: utf-8 -*-
"""分析每课 tests/bugs/reflection 数据差异"""
import io, re, json

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

# 找到课程数据数组起始
i = s.find('COURSE')
print('COURSE at', i)

# 找 sampleTestLab 渲染函数
j = s.find('function sampleTestLab')
print('sampleTestLab at', j)
print(s[j:j+1500])
