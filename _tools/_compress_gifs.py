# -*- coding: utf-8 -*-
"""压缩语雀GIF动图：宽度≤560、帧≤40、调色板优化 → assets/yuque_web/"""
import os
from PIL import Image, ImageSequence

SRC = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
DST = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque_web'
MAX_W = 560
MAX_FRAMES = 40

def compress_gif(src_path, dst_path):
    img = Image.open(src_path)
    frames = []
    durations = []
    total = getattr(img, 'n_frames', 1)
    # 帧采样
    step = max(1, total // MAX_FRAMES)
    idx = 0
    for frame in ImageSequence.Iterator(img):
        if idx % step == 0:
            f = frame.convert('RGBA')
            w, h = f.size
            if w > MAX_W:
                nh = int(h * MAX_W / w)
                f = f.resize((MAX_W, nh), Image.LANCZOS)
            frames.append(f.convert('P', palette=Image.ADAPTIVE, colors=192))
            durations.append(frame.info.get('duration', 100))
        idx += 1
    if not frames:
        return False
    frames[0].save(dst_path, save_all=True, append_images=frames[1:],
                   duration=durations[:len(frames)], loop=0, optimize=True, disposal=2)
    return True

count = 0
total_bytes = 0
for folder in ['basic', 'advanced', 'python']:
    d = os.path.join(SRC, folder)
    if not os.path.isdir(d):
        continue
    for fn in os.listdir(d):
        if not fn.lower().endswith(('.gif', '.gif.gif')):
            continue
        src = os.path.join(d, fn)
        base = fn.replace('.gif.gif', '.gif').replace('.gif', '')
        out = os.path.join(DST, folder, base + '.gif')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        try:
            sz_in = os.path.getsize(src)
            if compress_gif(src, out):
                sz_out = os.path.getsize(out)
                total_bytes += sz_out
                count += 1
                print(f'  {sz_in//1024:6d}KB -> {sz_out//1024:5d}KB  {os.path.basename(out)[:50]}')
            else:
                print(f'  SKIP(无帧) {fn}')
        except Exception as e:
            print(f'  ERR {fn}: {e}')
print(f'\n压缩完成 {count} 张，总大小 {total_bytes//1024//1024} MB')
