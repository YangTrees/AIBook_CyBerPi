# -*- coding: utf-8 -*-
"""第3课编程任务模块：transfer步骤1改为「复制闪烁程序」；并同步observe基准(0.5->1秒)"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

pairs = [
    # 编程任务 transfer 第一步
    ('复制闪烁程序，把灯的颜色改成红色', '复制闪烁程序'),
    # observe 基准与程序(等待1秒)保持一致
    ('等待时间从0.5秒改成2秒', '等待时间从1秒改成2秒'),
]
for old, new in pairs:
    n = s.count(old)
    print('count=%d  %s' % (n, old[:30]))
    assert n >= 1, old[:30]
    s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('done')
