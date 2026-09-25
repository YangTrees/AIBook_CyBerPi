# -*- coding: utf-8 -*-
"""生成GIF首帧contact sheet便于目检选图"""
import os
from PIL import Image

SRC = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
OUT = r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets'
os.makedirs(OUT, exist_ok=True)

for folder in ['basic', 'advanced', 'python']:
    d = os.path.join(SRC, folder)
    files = sorted([f for f in os.listdir(d) if f.lower().endswith('.gif')])
    thumbs = []
    labels = []
    for fn in files:
        p = os.path.join(d, fn)
        try:
            img = Image.open(p)
            f = img.convert('RGB')
            w, h = f.size
            if w > 320:
                f = f.resize((320, int(h * 320 / w)), Image.LANCZOS)
            thumbs.append(f)
            labels.append(fn[:28])
        except Exception as e:
            print('ERR', fn, e)
    if not thumbs:
        continue
    # 每行3个
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    cell_w, cell_h = 320, 240
    sheet = Image.new('RGB', (cols * cell_w, rows * cell_h), (245, 245, 245))
    from PIL import ImageDraw
    dr = ImageDraw.Draw(sheet)
    for i, (t, lb) in enumerate(zip(thumbs, labels)):
        r_, c_ = divmod(i, cols)
        x, y = c_ * cell_w, r_ * cell_h
        sheet.paste(t, (x + 10, y + 10))
        dr.text((x + 10, y + 215), lb, fill=(20, 20, 20))
    sheet.save(os.path.join(OUT, f'{folder}_sheet.jpg'), quality=80)
    print(f'{folder}: {len(thumbs)} 张 → sheet 保存')
