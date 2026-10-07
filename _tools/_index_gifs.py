# -*- coding: utf-8 -*-
"""分析语雀源动图：md5去重 + 抽帧拼图建立内容索引"""
import os, hashlib
from PIL import Image, ImageSequence

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
OUT = r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\sheets2\index'

os.makedirs(OUT, exist_ok=True)

def md5(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for ch in iter(lambda: f.read(1 << 20), b''):
            h.update(ch)
    return h.hexdigest()

groups = {}
rows = []
for folder in ['basic', 'advanced', 'python']:
    d = os.path.join(ROOT, folder)
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        p = os.path.join(d, fn)
        if not fn.lower().endswith('.gif'):
            continue
        try:
            im = Image.open(p)
            n = im.n_frames
        except Exception as e:
            n = -1
        m = md5(p)
        sz = os.path.getsize(p)
        groups.setdefault(m, []).append((folder, fn))
        rows.append((folder, fn, sz // 1024, n, m))

# 输出行
lines = []
for folder, fn, kb, n, m in rows:
    dup = len(groups[m])
    lines.append(f'{folder}/{fn} | {kb}KB | {n}帧 | md5={m[:8]} | 副本x{dup}')
io = open(os.path.join(OUT, 'index.txt'), 'w', encoding='utf-8')
io.write('\n'.join(lines))
io.close()

# 唯一文件抽帧拼图
uniq = {}
for folder, fn, kb, n, m in rows:
    if m not in uniq:
        uniq[m] = (folder, fn)

print(f'共 {len(rows)} 个gif，唯一 {len(uniq)} 个')
for gi, (m, (folder, fn)) in enumerate(sorted(uniq.items())):
    p = os.path.join(ROOT, folder, fn)
    try:
        im = Image.open(p)
        total = im.n_frames
        idxs = sorted(set([int(total * k / 6) for k in range(6)]))
        frames = []
        for i, fr in enumerate(ImageSequence.Iterator(im)):
            if i in idxs:
                f = fr.convert('RGB')
                if f.width > 300:
                    f = f.resize((300, int(f.height * 300 / f.width)), Image.LANCZOS)
                frames.append(f)
        if not frames:
            continue
        W = sum(f.width for f in frames)
        H = max(f.height for f in frames)
        sheet = Image.new('RGB', (W, H), (235, 235, 235))
        x = 0
        for f in frames:
            sheet.paste(f, (x, 0))
            x += f.width
        sheet.save(os.path.join(OUT, f'u{gi:03d}_{folder}_{fn[:40]}.jpg'), quality=80)
        print(f'u{gi:03d} {folder}/{fn} {total}帧 -> u{gi:03d}.jpg')
    except Exception as e:
        print('ERR', folder, fn, e)
print('DONE')
