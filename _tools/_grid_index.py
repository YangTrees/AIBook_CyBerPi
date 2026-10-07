# -*- coding: utf-8 -*-
"""把58张索引拼图拼成总览网格(带编号)"""
import os
from PIL import Image, ImageDraw

D = r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\index'
files = sorted([f for f in os.listdir(D) if f.startswith('u') and f.endswith('.jpg') and not f.startswith('grid')])
print('files:', len(files))

CELL = 240  # 每格宽
ROWS = 8
COLS = 8
W = COLS * CELL
H = ROWS * CELL
grid = Image.new('RGB', (W, H), (250, 250, 250))
dr = ImageDraw.Draw(grid)
for i, fn in enumerate(files):
    im = Image.open(os.path.join(D, fn))
    r, c = i // COLS, i % COLS
    # 缩放到适配格宽
    w = CELL - 8
    h = int(im.height * w / im.width)
    im2 = im.resize((w, h), Image.LANCZOS)
    grid.paste(im2, (c * CELL + 4, r * CELL + 4))
    dr.text((c * CELL + 6, r * CELL + 6), fn[:14], fill=(255, 0, 0))
grid.save(os.path.join(D, 'grid_all.jpg'), quality=82)
print('saved grid_all.jpg', grid.size)
