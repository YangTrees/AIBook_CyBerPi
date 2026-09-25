# -*- coding: utf-8 -*-
"""按map_json补下载缺失文件"""
import json, os, re, urllib.request, time

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi'
TOOLS = os.path.join(ROOT, '_tools')
OUT = os.path.join(ROOT, 'AI编程探险课_CyberPi', 'assets', 'yuque')
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36'}

def existing_uuids(folder):
    d = os.path.join(OUT, folder)
    if not os.path.isdir(d):
        return set()
    s = set()
    for fn in os.listdir(d):
        s.add(fn.split('_', 1)[-1].split('.')[0])
    return s

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

count = 0
for folder, mapname in [('basic', 'map_basic.json'), ('advanced', 'map_advanced.json'), ('python', 'map_python.json')]:
    items = json.load(open(os.path.join(TOOLS, mapname), encoding='utf-8'))
    exist = existing_uuids(folder)
    seen = set()
    for it in items:
        u = it['img']
        if u in seen:
            continue
        seen.add(u)
        clean = u.split('?')[0]
        uuid_full = clean.rstrip('/').split('/')[-1]
        uuid = uuid_full.split('.')[0]
        if uuid in exist:
            continue
        m = re.search(r'\.(gif|jpe?g|png|webp)(?=$|/)', clean, re.I)
        ext = (m.group(1) if m else 'img').lower()
        if ext == 'jpeg':
            ext = 'jpg'
        d = os.path.join(OUT, folder)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, f'{uuid}.{ext}')
        try:
            data = fetch(u)
            with open(path, 'wb') as f:
                f.write(data)
            print(f'  +{len(data)//1024}KB {os.path.basename(path)[:60]}')
            count += 1
        except Exception as e:
            print(f'  ERR {u[:80]} -> {e}')
        time.sleep(0.15)
print(f'补下载 {count} 个文件')
