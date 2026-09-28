# -*- coding: utf-8 -*-
"""第3课积木程序模块：等待0.5秒 -> 等待1秒（仅第3课，不影响第19课心跳/第24课计步器）"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

pairs = [
    # blocks 积木（第3课上下文唯一）
    ('["灯","RGB灯亮起 红色"],["等待","等待0.5秒"],["灯","RGB灯熄灭"],["等待","等待0.5秒"]',
     '["灯","RGB灯亮起 红色"],["等待","等待1秒"],["灯","RGB灯熄灭"],["等待","等待1秒"]'),
    # steps 第5/6步
    ('放入「等待0.5秒」，再放入「RGB灯熄灭」', '放入「等待1秒」，再放入「RGB灯熄灭」'),
    ('放入「等待0.5秒」，点击上传，观察灯带持续闪烁', '放入「等待1秒」，点击上传，观察灯带持续闪烁'),
    # SAMPLE_CONTENT stepTitles 第3课
    ('放入「等待0.5秒」，再…', '放入「等待1秒」，再…'),
    # curriculum 3 watch（描述亮灭时长，保持一致）
    ('亮0.5秒、灭0.5秒，是不是很均匀', '亮1秒、灭1秒，是不是很均匀'),
]
for old, new in pairs:
    n = s.count(old)
    print('count=%d  %s' % (n, old[:30]))
    assert n >= 1, old[:30]
    s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('done')
