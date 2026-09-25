# -*- coding: utf-8 -*-
"""抽重压后GIF的帧验证颜色"""
import sys
from PIL import Image, ImageSequence

def montage(path, out, n=4):
    img = Image.open(path)
    total = img.n_frames
    idxs = sorted(set([int(total * k / n) for k in range(n)]))
    frames = []
    for i, fr in enumerate(ImageSequence.Iterator(img)):
        if i in idxs:
            f = fr.convert('RGB')
            if f.width > 360:
                f = f.resize((360, int(f.height * 360 / f.width)), Image.LANCZOS)
            frames.append(f)
    W = sum(f.width for f in frames)
    H = max(f.height for f in frames)
    sheet = Image.new('RGB', (W, H), (240, 240, 240))
    x = 0
    for f in frames:
        sheet.paste(f, (x, 0))
        x += f.width
    sheet.save(out, quality=85)
    print(f'{path.split("/")[-1]}: {total}帧 -> {out}')

montage(r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_web\lesson-05.gif',
        r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\verify_l05.jpg')
montage(r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_web\lesson-12.gif',
        r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\verify_l12.jpg')
montage(r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_web\lesson-16.gif',
        r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\verify_l16.jpg')
