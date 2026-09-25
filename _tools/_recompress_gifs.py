# -*- coding: utf-8 -*-
"""重压32课动图：全局统一调色板（MEDIANCUT），修复色板闪烁花屏"""
import os
from PIL import Image, ImageSequence

SRC = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
DST = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_web'
MAX_W = 520
MAX_FRAMES = 32
COLORS = 192

PICKS = {
    1: ('basic', '1655883861810'),
    2: ('basic', '1655883901785'),
    3: ('basic', '1655883901814'),
    4: ('basic', '1655884072826'),
    5: ('basic', '1655884791545'),
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
    26: ('basic', '1655884828878'),
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

total_bytes = 0
for lid, (folder, uuid) in sorted(PICKS.items()):
    p = find(folder, uuid)
    if not p:
        print('MISS', lid, uuid)
        continue
    im = Image.open(p)
    total = im.n_frames
    step = max(1, total // MAX_FRAMES)
    frames_rgb, durations = [], []
    idx = 0
    for fr in ImageSequence.Iterator(im):
        if idx % step == 0:
            f = fr.convert('RGB')
            w, h = f.size
            if w > MAX_W:
                f = f.resize((MAX_W, int(h * MAX_W / w)), Image.LANCZOS)
            frames_rgb.append(f)
            durations.append(fr.info.get('duration', 100))
        idx += 1
    if not frames_rgb:
        print('EMPTY', lid)
        continue
    # 全局调色板：以第一帧量化生成，其余帧映射到同一调色板
    pal = frames_rgb[0].quantize(colors=COLORS, method=Image.MEDIANCUT)
    frames_p = [f.quantize(palette=pal) for f in frames_rgb]
    out = os.path.join(DST, f'lesson-{lid:02d}.gif')
    frames_p[0].save(out, save_all=True, append_images=frames_p[1:],
                     duration=durations[:len(frames_p)], loop=0, optimize=True, disposal=1)
    kb = os.path.getsize(out) // 1024
    total_bytes += kb
    print(f'L{lid:02d}: {kb}KB ({len(frames_p)}帧)')
print(f'总计 {total_bytes//1024} MB')
