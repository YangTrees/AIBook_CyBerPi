# -*- coding: utf-8 -*-
"""下载语雀图片/动图到 assets/yuque/{basic,advanced,python}/"""
import os, re, urllib.request, urllib.parse, time

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi'
TOOLS = os.path.join(ROOT, '_tools')
OUT = os.path.join(ROOT, 'AI编程探险课_CyberPi', 'assets', 'yuque')

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def save(url, folder, idx):
    # 去参数（如 ?x-oss-process=...）得到原始文件名
    clean = url.split('?')[0]
    m = re.search(r'\.(gif|jpe?g|png|webp)(?=$|/)', clean, re.I)
    ext = (m.group(1) if m else 'img').lower()
    if ext == 'jpeg':
        ext = 'jpg'
    d = os.path.join(OUT, folder)
    os.makedirs(d, exist_ok=True)
    # 用 uuid 片段命名，保留序号便于排序
    uuid = clean.rstrip('/').split('/')[-1]
    name = f'{idx:02d}_{uuid}.{ext}'
    path = os.path.join(d, name)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path, 'skip'
    data = fetch(url)
    with open(path, 'wb') as f:
        f.write(data)
    return path, f'{len(data)//1024}KB'

total = 0
for folder, fname in [('basic', 'yuque_basic_urls.txt'), ('advanced', 'yuque_advanced_urls.txt'), ('python', 'yuque_python_urls.txt')]:
    urls = [l.strip() for l in open(os.path.join(TOOLS, fname), encoding='utf-8') if l.strip()]
    print(f'--- {folder}: {len(urls)} 个 URL ---')
    seen = set()
    for idx, u in enumerate(urls, 1):
        if u in seen:
            continue
        seen.add(u)
        try:
            p, info = save(u, folder, idx)
            print(f'  {info:8s} {os.path.basename(p)}')
            total += 1
        except Exception as e:
            print(f'  ERR {u[:80]} -> {e}')
        time.sleep(0.2)
print(f'\n完成，共下载 {total} 个文件')
