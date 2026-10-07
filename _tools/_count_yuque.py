# -*- coding: utf-8 -*-
"""统计 assets/yuque 素材类型分布"""
import os

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
exts = {}
total = 0
for folder in ['basic', 'advanced', 'python']:
    d = os.path.join(ROOT, folder)
    if not os.path.isdir(d):
        print('缺失目录:', d)
        continue
    for fn in os.listdir(d):
        ext = fn.rsplit('.', 1)[-1].lower() if '.' in fn else 'none'
        exts.setdefault(folder + '/' + ext, 0)
        exts[folder + '/' + ext] += 1
        total += 1
for k in sorted(exts):
    print(k, exts[k])
print('TOTAL', total)
