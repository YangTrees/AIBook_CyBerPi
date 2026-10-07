# -*- coding: utf-8 -*-
"""更新 .gitignore：排除超大原始素材与临时产物"""
import io
p = r'D:\PROJECTS\_AI\AIBook_CyberPi\.gitignore'
s = io.open(p, encoding='utf-8').read()
add = '''
# 语雀原始素材（数百MB，不入库；网页仅引用 yuque_web 压缩版）
AI编程探险课_CyberPi/assets/yuque/
AI编程探险课_CyberPi/bak_index_gif.html

# 工具临时产物
_tools/sheets/
_tools/sheets2/
_tools/*_out.txt
'''
if 'yuque_web' not in s:
    s += add
io.open(p, 'w', encoding='utf-8').write(s)
print('gitignore updated')
