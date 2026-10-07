# -*- coding: utf-8 -*-
"""提取3课(1/12/25)的 tests/bugs/reflection 数据做对比"""
import io, re

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

# 找到 taskSpec 函数
i = s.find('function taskSpec')
print('taskSpec at', i)
print(s[i:i+2000])
