# -*- coding: utf-8 -*-
"""把 yuque_web 未引用子目录加入 .gitignore"""
import io
p = r'D:\PROJECTS\_AI\AIBook_CyberPi\.gitignore'
s = io.open(p, encoding='utf-8').read()
add = '''
# 未引用素材子目录（网页仅用 lesson-XX.gif）
AI编程探险课_CyberPi/assets/yuque_web/basic/
AI编程探险课_CyberPi/assets/yuque_web/advanced/
AI编程探险课_CyberPi/assets/yuque_web/python/
'''
if 'yuque_web/basic' not in s:
    s += add
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
