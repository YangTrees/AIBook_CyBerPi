# -*- coding: utf-8 -*-
"""生成32课选定动图总览拼图（中间帧）"""
import os
from PIL import Image, ImageSequence, ImageDraw

SRC = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
SH = r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2'
os.makedirs(SH, exist_ok=True)

# 课号 -> (folder, uuid)
PICKS = {
    1: ('basic', '1655883861810'),
    2: ('basic', '1655883901785'),
    3: ('basic', '1655883901814'),
    4: ('basic', '1655884020267'),
    5: ('basic', '1655884829100'),
    6: ('basic', '1655884117184'),
    7: ('basic', '1655884186110'),
    8: ('basic', '1655884413675'),
    9: ('basic', '1655884828878'),
    10: ('basic', '1655885681598'),
    11: ('python', '1672885955910'),
    12: ('advanced', '1655887064046'),
    13: ('advanced', '1655886525065'),
    14: ('advanced', '1655886525034'),
    15: ('advanced', '1655887362055'),
    16: ('python', '1672886426332'),
    17: ('advanced', '1655886830074'),
    18: ('advanced', '1655886842347'),
    19: ('advanced', '1655887645229'),
    20: ('advanced', '1655886976660'),
    21: ('advanced', '1655887930648'),
    22: ('advanced', '1655887016936'),
    23: ('basic', '1655884828920'),
    24: ('python', '1672887576956'),
    25: ('python', '1672886395242'),
    26: ('basic', '1655884791545'),
    27: ('python', '1672887335188'),
    28: ('advanced', '1655887012993'),
    29: ('basic', '1655884877204'),
    30: ('python', '1672888257920'),
    31: ('advanced', '1655886829999'),
    32: ('python', '1672888031080'),
}

def find(folder, uuid):
    d = os.path.join(SRC, folder)
    for fn in os.listdir(d):
        if uuid in fn:
            return os.path.join(d, fn)
    return None

def mid_frame(path, w=420):
    img = Image.open(path)
    total = img.n_frames
    idx = total // 2
    for i, fr in enumerate(ImageSequence.Iterator(img)):
        if i == idx:
            f = fr.convert('RGB')
            if f.width > w:
                f = f.resize((w, int(f.height * w / f.width)), Image.LANCZOS)
            return f, total, os.path.getsize(path) // 1024
    return None, total, 0

cols = 4
cell_w, cell_h = 430, 260
rows = (len(PICKS) + cols - 1) // cols
sheet = Image.new('RGB', (cols * cell_w, rows * cell_h), (250, 250, 250))
dr = ImageDraw.Draw(sheet)
for i, (lid, (folder, uuid)) in enumerate(sorted(PICKS.items())):
    p = find(folder, uuid)
    if not p:
        print('MISS', lid, uuid)
        continue
    f, total, kb = mid_frame(p)
    if f is None:
        print('FAIL', lid, p)
        continue
    r_, c_ = divmod(i, cols)
    x, y = c_ * cell_w, r_ * cell_h
    sheet.paste(f, (x + 5, y + 5))
    dr.text((x + 5, y + cell_h - 20), f'L{lid:02d} {kb}KB {total}帧', fill=(10, 10, 10))
out = os.path.join(SH, 'picks_overview.jpg')
sheet.save(out, quality=84)
print('saved', out)
