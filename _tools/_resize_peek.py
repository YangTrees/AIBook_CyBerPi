# -*- coding: utf-8 -*-
"""将大拼图缩小后拆分查看"""
from PIL import Image
import os
for tag in ['effect_l28_frames', 'step_l28_frames']:
    fp = os.path.join(r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools', tag + '.jpg')
    im = Image.open(fp)
    w, h = im.size
    # 缩小到 <=3200 宽
    scale = 3200 / w
    im2 = im.resize((int(w*scale), int(h*scale)))
    out = os.path.join(r'D:\PROJECTS\_AI\AIBook_CyberPi\_tools', tag + '_small.jpg')
    im2.save(out, quality=82)
    print(tag, '->', im2.size, out)
