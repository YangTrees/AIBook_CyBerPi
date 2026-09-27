# -*- coding: utf-8 -*-
"""统计原图尺寸/帧数/体积（效果动图32 + 步骤动图24）"""
import os, io, json
from PIL import Image

BASE = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'

# 32课效果动图源（folder, uuid）—— 从 _recompress_gifs_v3.py 的 PICKS 提取
picks = {
 1:('basic','1655883861810'), 2:('basic','1655883901785'), 3:('basic','1655883901814'),
 4:('basic','1655884072826'), 5:('basic','1655884791545'), 6:('basic','1655884117184'),
 7:('basic','1655884186110'), 8:('basic','1655884413675'), 9:('basic','1655884828878'),
 10:('basic','1655885681598'), 11:('python','1672885955910'), 12:('advanced','1655887064046'),
 13:('advanced','1655886525065'), 14:('advanced','1655886525034'), 15:('advanced','1655887362055'),
 16:('python','1672886426332'), 17:('advanced','1655886830074'), 18:('advanced','1655886842347'),
 19:('advanced','1655887645229'), 20:('advanced','1655886976660'), 21:('advanced','1655887930648'),
 22:('advanced','1655887016936'), 23:('basic','1655884828920'), 24:('python','1672887576956'),
 25:('python','1672886395242'), 26:('basic','1655884828878'), 27:('python','1672887335188'),
 28:('advanced','1655887012993'), 29:('basic','1655884877204'), 30:('python','1672888257920'),
 31:('advanced','1655886829999'), 32:('python','1672888031080'),
}
steps = {
 1:('basic','1655883861775'), 2:('advanced','1655886335984'), 3:('basic','1655883923090'),
 4:('basic','1655884077888'), 5:('basic','1655884828920'), 6:('basic','1655884157534'),
 7:('basic','1655884376973'), 8:('basic','1655884637391'), 9:('basic','1655884828920'),
 10:('basic','1655884877198'), 11:('advanced','1655886335984'), 12:('advanced','1655887056514'),
 13:('advanced','1655886524988'), 14:('advanced','1655886788597'), 15:('advanced','1655887362055'),
 16:('advanced','1655887493300'), 17:('advanced','1655888217067'), 18:('advanced','1655886842347'),
 19:('advanced','1655887645229'), 20:('advanced','1655886981336'), 21:('advanced','1655886976625'),
 22:('advanced','1655887050863'), 25:('advanced','1655887493300'), 28:('advanced','1655887013148'),
 29:('basic','1655884918538'),
}

def find(folder, uuid):
    d = os.path.join(BASE, folder)
    for fn in os.listdir(d):
        if uuid in fn:
            return os.path.join(d, fn)
    return None

def stat(name, mapping):
    total = 0
    rows = []
    for lid in sorted(mapping):
        folder, uuid = mapping[lid]
        p = find(folder, uuid)
        if not p:
            rows.append((lid, 'MISS', 0, 0, 0))
            continue
        sz = os.path.getsize(p)
        total += sz
        try:
            im = Image.open(p)
            w, h = im.size
            n = im.n_frames
            rows.append((lid, os.path.basename(p)[:30], w, h, n, sz//1024))
        except Exception as e:
            rows.append((lid, os.path.basename(p)[:30], -1, -1, -1, sz//1024))
    print(f'== {name}: {len(rows)} 个，总体积 {total//1024//1024} MB ==')
    for r in rows:
        print(r)
    return total

stat('效果动图(32)', picks)
stat('步骤动图(24)', steps)
