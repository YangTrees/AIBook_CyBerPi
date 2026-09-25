# -*- coding: utf-8 -*-
"""为每课候选动图生成中间帧拼图（排除连接动画与设备图）"""
import os, json
from PIL import Image, ImageSequence, ImageDraw

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi'
TOOLS = os.path.join(ROOT, '_tools')
SRC = os.path.join(ROOT, 'AI编程探险课_CyberPi', 'assets', 'yuque')
SH = os.path.join(TOOLS, 'sheets2')
os.makedirs(SH, exist_ok=True)

# 连接动画的uuid（MD5相同的22个）
CONNECT_UUIDS = {
    '1655888074199', '1655886342518', '1655886788822', '1655886830086',
    '1655886550524', '1655886863134', '1655886525260', '1655884420340',
    '1655884329043', '1655883862127', '1655883902160', '1655884117644',
    '1655884020267', '1655884829100', '1655884877441', '1655884877428',
    '1655887584929', '1655887946503', '1655886977468', '1655887012889',
    '1655887048714', '1655887064046'  # 部分可能不准，按MD5组取
}

def frame_mid(path, w=360):
    img = Image.open(path)
    total = img.n_frames
    idx = total // 2
    for i, fr in enumerate(ImageSequence.Iterator(img)):
        if i == idx:
            f = fr.convert('RGB')
            if f.width > w:
                f = f.resize((w, int(f.height * w / f.width)), Image.LANCZOS)
            return f, total
    return None, total

def build(folder, mapname, outname, max_items=30):
    items = json.load(open(os.path.join(TOOLS, mapname), encoding='utf-8'))
    cur = ''
    rows = []  # (sec, img_path, frames, size)
    seen = set()
    for it in items:
        u = it['img']
        cur = it['sec']
        clean = u.split('?')[0]
        uuid = clean.rstrip('/').split('/')[-1].split('.')[0]
        if uuid in seen or uuid in CONNECT_UUIDS:
            continue
        seen.add(uuid)
        # 找本地文件
        d = os.path.join(SRC, folder)
        hit = None
        for fn in os.listdir(d):
            if uuid in fn:
                hit = os.path.join(d, fn)
                break
        if not hit:
            continue
        size = os.path.getsize(hit) // 1024
        rows.append((cur, hit, size))
    # 生成拼图：每行1个候选（中间帧）
    cols = 3
    cell_w, cell_h = 380, 240
    n = min(len(rows), max_items)
    sheet = Image.new('RGB', (cols * cell_w, ((n + cols - 1) // cols) * cell_h), (248, 248, 248))
    dr = ImageDraw.Draw(sheet)
    for i, (sec, path, size) in enumerate(rows[:n]):
        try:
            f, total = frame_mid(path)
        except Exception:
            continue
        if f is None:
            continue
        r_, c_ = divmod(i, cols)
        x, y = c_ * cell_w, r_ * cell_h
        sheet.paste(f, (x + 8, y + 8))
        dr.text((x + 8, y + cell_h - 18), f'{os.path.basename(path)[:34]} | {size}KB {total}帧', fill=(15, 15, 15))
    out = os.path.join(SH, outname)
    sheet.save(out, quality=82)
    print(f'{outname}: 候选{len(rows)}张（显示前{n}）')

build('basic', 'map_basic.json', 'basic_cand.jpg')
build('advanced', 'map_advanced.json', 'advanced_cand.jpg')
build('python', 'map_python.json', 'python_cand.jpg')
