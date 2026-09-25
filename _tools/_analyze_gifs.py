# -*- coding: utf-8 -*-
"""分析3个map，生成 语雀课程→动图 候选清单"""
import json, os, re

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi'
TOOLS = os.path.join(ROOT, '_tools')

def load(name):
    return json.load(open(os.path.join(TOOLS, name), encoding='utf-8'))

basic = load('map_basic.json')
advanced = load('map_advanced.json')
python = load('map_python.json')

def group(items):
    """按 sec 分组"""
    g = {}
    for it in items:
        g.setdefault(it['sec'], []).append(it['img'])
    return g

def is_gif(url):
    return '.gif' in url.split('?')[0]

for tag, items in [('BASIC', basic), ('ADVANCED', advanced), ('PYTHON', python)]:
    print(f'===== {tag} =====')
    for sec, urls in group(items).items():
        gifs = [u for u in urls if is_gif(u)]
        non_gifs = [u for u in urls if not is_gif(u)]
        print(f'  [{sec[:24]}] 共{len(urls)} 动图{len(gifs)}')
        for u in gifs:
            print(f'      GIF: ...{u.split("?")[0].split("/")[-1][:40]}')
