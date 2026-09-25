# -*- coding: utf-8 -*-
"""压缩语雀Part3步骤动图 -> assets/yuque_steps/lesson-XX/step-02.{gif|png}"""
import os
from PIL import Image, ImageSequence

SRC = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
DST = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_steps'
MAX_W = 560
MAX_FRAMES = 30
COLORS = 256

MATCH = {
    1: ('basic', '1655883861775'),
    2: ('advanced', '1655886335984'),
    3: ('basic', '1655883923090'),
    4: ('basic', '1655884077888'),
    5: ('basic', '1655884828920'),
    6: ('basic', '1655884157534'),
    7: ('basic', '1655884376973'),
    8: ('basic', '1655884637391'),
    9: ('basic', '1655884828920'),
    10: ('basic', '1655884877198'),
    11: ('advanced', '1655886335984'),
    12: ('advanced', '1655887056514'),
    13: ('advanced', '1655886524988'),
    14: ('advanced', '1655886788597'),
    15: ('advanced', '1655887362055'),
    16: ('advanced', '1655887493300'),
    17: ('advanced', '1655888217067'),
    18: ('advanced', '1655886842347'),
    19: ('advanced', '1655887645229'),
    20: ('advanced', '1655886981336'),
    21: ('advanced', '1655886976625'),
    22: ('advanced', '1655887050863'),
    25: ('advanced', '1655887493300'),
    28: ('advanced', '1655887013148'),
    29: ('basic', '1655884918538'),
}

def find(folder, uuid):
    d = os.path.join(SRC, folder)
    for fn in os.listdir(d):
        if uuid in fn:
            return os.path.join(d, fn)
    return None

def compress_gif(src, dst, max_w=MAX_W, max_frames=MAX_FRAMES, colors=COLORS):
    im = Image.open(src)
    total = im.n_frames
    step = max(1, total // max_frames)
    frames_rgb, durations, samples = [], [], []
    idx = 0
    for fr in ImageSequence.Iterator(im):
        if idx % step == 0:
            f = fr.convert('RGB')
            w, h = f.size
            if w > max_w:
                f = f.resize((max_w, int(h * max_w / w)), Image.LANCZOS)
            frames_rgb.append(f)
            durations.append(fr.info.get('duration', 100))
            sm = f.resize((32, max(1, int(32 * f.height / f.width))), Image.LANCZOS)
            samples.append(list(sm.getdata()))
        idx += 1
    if not frames_rgb:
        return False
    flat = [px for smp in samples for px in smp]
    pal_img = Image.new('RGB', (len(flat), 1))
    pal_img.putdata(flat)
    pal = pal_img.quantize(colors=colors, method=Image.MEDIANCUT)
    frames_p = [f.quantize(palette=pal) for f in frames_rgb]
    frames_p[0].save(dst, save_all=True, append_images=frames_p[1:],
                     duration=durations[:len(frames_p)], loop=0, optimize=True, disposal=1)
    return True

def compress_png(src, dst, max_w=MAX_W):
    im = Image.open(src).convert('RGB')
    w, h = im.size
    if w > max_w:
        im = im.resize((max_w, int(h * max_w / w)), Image.LANCZOS)
    im.save(dst, quality=88)
    return True

total_kb = 0
for lid, (folder, uuid) in sorted(MATCH.items()):
    src = find(folder, uuid)
    if not src:
        print('MISS', lid); continue
    ldir = os.path.join(DST, f'lesson-{lid:02d}')
    os.makedirs(ldir, exist_ok=True)
    is_png = src.lower().endswith('.png')
    ext = 'png' if is_png else 'gif'
    dst = os.path.join(ldir, f'step-02.{ext}')
    ok = compress_png(src, dst) if is_png else compress_gif(src, dst)
    if ok:
        kb = os.path.getsize(dst) // 1024
        total_kb += kb
        print(f'L{lid:>2}: {kb}KB ({ext})')
    else:
        print(f'L{lid:>2}: FAIL')
print(f'TOTAL {total_kb//1024} MB')
