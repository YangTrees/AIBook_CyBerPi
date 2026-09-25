# -*- coding: utf-8 -*-
"""测试：全部帧合并采样生成调色板，保留彩色"""
from PIL import Image, ImageSequence

def build(src, dst, max_w=520, colors=256):
    im = Image.open(src)
    total = im.n_frames
    step = max(1, total // 36)
    frames_rgb, durations = [], []
    samples = []
    idx = 0
    for fr in ImageSequence.Iterator(im):
        if idx % step == 0:
            f = fr.convert('RGB')
            w, h = f.size
            if w > max_w:
                f = f.resize((max_w, int(h * max_w / w)), Image.LANCZOS)
            frames_rgb.append(f)
            durations.append(fr.info.get('duration', 100))
            # 采样：缩到32x18取像素
            sm = f.resize((32, max(1, int(32 * f.height / f.width))), Image.LANCZOS)
            samples.append(list(sm.getdata()))
        idx += 1
    # 合并所有采样生成调色板
    flat = [p for s in samples for p in s]
    pal_img = Image.new('RGB', (len(flat), 1))
    pal_img.putdata(flat)
    pal = pal_img.quantize(colors=colors, method=Image.MEDIANCUT)
    frames_p = [f.quantize(palette=pal) for f in frames_rgb]
    frames_p[0].save(dst, save_all=True, append_images=frames_p[1:],
                     duration=durations[:len(frames_p)], loop=0, optimize=True, disposal=1)
    import os
    print(f'{dst.split("/")[-1]}: {os.path.getsize(dst)//1024}KB {len(frames_p)}帧')

src = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque\basic\06_1655883901785-75d58ae8-7624-4fca-9e79-5d39f9cdeaed.gif.gif'
dst = r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\test_l02_256.jpg.gif'
build(src, dst)

# 抽帧验证
im = Image.open(dst)
idxs = sorted(set([int(im.n_frames * k / 4) for k in range(4)]))
frames = []
for i, fr in enumerate(ImageSequence.Iterator(im)):
    if i in idxs:
        f = fr.convert('RGB')
        frames.append(f)
W = sum(f.width for f in frames)
H = max(f.height for f in frames)
sheet = Image.new('RGB', (W, H), (235, 235, 235))
x = 0
for f in frames:
    sheet.paste(f, (x, 0)); x += f.width
sheet.save(r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\test_l02_256_check.jpg', quality=90)
print('saved check')
