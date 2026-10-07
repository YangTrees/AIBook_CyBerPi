# -*- coding: utf-8 -*-
"""检查 lesson-02.gif 实际内容与源对应关系"""
from PIL import Image, ImageSequence
import os

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_web\lesson-02.gif'
im = Image.open(p)
print('lesson-02.gif 帧数:', im.n_frames, '尺寸:', im.size)

# 抽 4 帧拼图
idxs = sorted(set([int(im.n_frames * k / 4) for k in range(4)]))
frames = []
for i, fr in enumerate(ImageSequence.Iterator(im)):
    if i in idxs:
        f = fr.convert('RGB')
        frames.append(f)
W = sum(f.width for f in frames)
H = max(f.height for f in frames)
sheet = Image.new('RGB', (W, H), (235, 235, 235))
x = 0
for f in frames:
    sheet.paste(f, (x, 0)); x += f.width
out = r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\l02_now.jpg'
sheet.save(out, quality=85)
print('saved', out)

# 检查源目录中匹配 1655883901785 的文件
SRC = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque\basic'
for fn in os.listdir(SRC):
    if '1655883901785' in fn:
        q = os.path.join(SRC, fn)
        qi = Image.open(q)
        print('源匹配:', fn, '帧数:', qi.n_frames, '大小:', os.path.getsize(q)//1024, 'KB')
