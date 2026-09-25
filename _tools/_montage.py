# -*- coding: utf-8 -*-
"""抽GIF第1/中/尾帧拼图查看内容"""
import sys, os
from PIL import Image, ImageSequence

def montage(path, out, n=3):
    img = Image.open(path)
    total = img.n_frames
    idxs = sorted(set([0, total // 2, total - 1]))[:n]
    frames = []
    for i, fr in enumerate(ImageSequence.Iterator(img)):
        if i in idxs:
            f = fr.convert('RGB')
            if f.width > 400:
                f = f.resize((400, int(f.height * 400 / f.width)), Image.LANCZOS)
            frames.append(f)
    W = sum(f.width for f in frames)
    H = max(f.height for f in frames)
    sheet = Image.new('RGB', (W, H), (250, 250, 250))
    x = 0
    for f in frames:
        sheet.paste(f, (x, 0))
        x += f.width
    sheet.save(out, quality=82)
    print(f'{os.path.basename(path)[:50]}: {total}帧 → {out}')

# 22个相同文件之一
p1 = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque\advanced\01_1655888074199-a547c7ea-fe46-4232-8195-53d707b5e55d.gif.gif'
montage(p1, r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets\dup_big.gif.jpg')
# 摇杆课程15MB
p2 = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque\basic\1655885681598-2f9fe9de-e06b-44ee-8605-58c90a4dc1bf.gif'
montage(p2, r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets\joystick_big.gif.jpg')
