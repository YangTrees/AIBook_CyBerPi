# -*- coding: utf-8 -*-
"""确认语雀 Part3 步骤动图是否在本地 assets/yuque 中"""
import os

SRC = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque'
# lessonId -> (folder, uuid)
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
for lid, (folder, uuid) in sorted(MATCH.items()):
    d = os.path.join(SRC, folder)
    hit = [fn for fn in os.listdir(d) if uuid in fn]
    print(f'L{lid:>2} {folder}/{uuid}: {"OK " + hit[0][:60] if hit else "MISSING"}')
