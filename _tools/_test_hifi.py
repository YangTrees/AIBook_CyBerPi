# -*- coding: utf-8 -*-
"""测试：PIL高保真重存 vs 原样拷贝"""
import os, shutil
from PIL import Image, ImageSequence

BASE = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\yuque\basic'
SRC = [os.path.join(BASE, fn) for fn in os.listdir(BASE) if '1655883901785' in fn][0]
print('源文件:', os.path.basename(SRC))

DST = r'C:\Users\YL\AppData\Local\Temp\test_hifi'
os.makedirs(DST, exist_ok=True)
print('原图:', os.path.getsize(SRC)//1024, 'KB')

im = Image.open(SRC)
durs = []
for fr in ImageSequence.Iterator(im):
    durs.append(fr.info.get('duration', 100))
print('帧数:', len(durs), '尺寸:', im.size)

# B1: 逐帧 copy + optimize
frames = []
for fr in ImageSequence.Iterator(im):
    f = fr.copy()
    f.info = {}
    frames.append(f)
b1 = os.path.join(DST, 'b1_optimize.gif')
frames[0].save(b1, save_all=True, append_images=frames[1:], duration=durs, loop=0, optimize=True)
print('B1 optimize:', os.path.getsize(b1)//1024, 'KB')

# B2: RGB->P自适应色板
frames2 = []
for fr in ImageSequence.Iterator(im):
    frames2.append(fr.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=256))
b2 = os.path.join(DST, 'b2_p.gif')
frames2[0].save(b2, save_all=True, append_images=frames2[1:], duration=durs, loop=0, optimize=True)
print('B2 P模式:', os.path.getsize(b2)//1024, 'KB')

c = os.path.join(DST, 'copy.gif')
shutil.copy2(SRC, c)
print('copy:', os.path.getsize(c)//1024, 'KB')
