# -*- coding: utf-8 -*-
"""第28课素材检查：抽帧拼图查看官方效果动图/搭建动图内容"""
from PIL import Image
import os

base = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets'
files = {
    'effect': os.path.join(base, 'yuque_web', 'lesson-28.gif'),
    'step': os.path.join(base, 'yuque_steps', 'lesson-28', 'step-02.gif'),
}
for tag, fp in files.items():
    if not os.path.exists(fp):
        print(tag, 'MISSING', fp)
        continue
    im = Image.open(fp)
    n = getattr(im, 'n_frames', 1)
    # 均匀抽 6 帧
    idxs = [int(i * (n-1) / 6) for i in range(6)] + [n-1]
    idxs = sorted(set(idxs))
    frames = []
    for i in idxs:
        im.seek(i)
        frames.append(im.convert('RGB').copy())
    w, h = frames[0].size
    grid = Image.new('RGB', (w*len(frames), h), 'white')
    for k, f in enumerate(frames):
        grid.paste(f, (k*w, 0))
    out = os.path.join(r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools', tag + '_l28_frames.jpg')
    grid.save(out, quality=80)
    print(tag, 'frames=%d size=%dx%d grid=%s' % (n, w, h, out))
