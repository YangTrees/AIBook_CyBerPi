# -*- coding: utf-8 -*-
"""验证v3重压后彩色保留"""
from PIL import Image, ImageSequence
import os

DST = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_web'
OUT = r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2'

def montage(lid, outname, n=4):
    p = os.path.join(DST, f'lesson-{lid:02d}.gif')
    im = Image.open(p)
    total = im.n_frames
    idxs = sorted(set([int(total * k / n) for k in range(n)]))
    frames = []
    for i, fr in enumerate(ImageSequence.Iterator(im)):
        if i in idxs:
            f = fr.convert('RGB')
            if f.width > 340:
                f = f.resize((340, int(f.height * 340 / f.width)), Image.LANCZOS)
            frames.append(f)
    W = sum(f.width for f in frames)
    H = max(f.height for f in frames)
    sheet = Image.new('RGB', (W, H), (235, 235, 235))
    x = 0
    for f in frames:
        sheet.paste(f, (x, 0)); x += f.width
    sheet.save(os.path.join(OUT, outname), quality=90)
    print(f'L{lid:02d} ({total}帧) -> {outname}')

for lid, name in [(2, 'v3_l02.jpg'), (12, 'v3_l12.jpg'), (13, 'v3_l13.jpg'), (18, 'v3_l18.jpg')]:
    montage(lid, name)
