# -*- coding: utf-8 -*-
"""用语雀原图替换压缩版：效果动图 yuque_web/lesson-XX.gif + 步骤图 yuque_steps/lesson-XX/step-02.*"""
import os, shutil

BASE = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets'
YUQUE = os.path.join(BASE, 'yuque')
WEB = os.path.join(BASE, 'yuque_web')
STEPS = os.path.join(BASE, 'yuque_steps')

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
    d = os.path.join(YUQUE, folder)
    for fn in os.listdir(d):
        if uuid in fn:
            return os.path.join(d, fn)
    return None

def copy_to(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    return os.path.getsize(dst)//1024

tot = 0
# 效果动图
for lid in sorted(picks):
    folder, uuid = picks[lid]
    src = find(folder, uuid)
    dst = os.path.join(WEB, f'lesson-{lid:02d}.gif')
    kb = copy_to(src, dst)
    tot += kb
    print(f'web L{lid:>2}: {kb}KB')
# 步骤图
for lid in sorted(steps):
    folder, uuid = steps[lid]
    src = find(folder, uuid)
    ext = 'png' if src.lower().endswith('.png') else 'gif'
    dst = os.path.join(STEPS, f'lesson-{lid:02d}', f'step-02.{ext}')
    kb = copy_to(src, dst)
    tot += kb
    print(f'step L{lid:>2}: {kb}KB ({ext})')
print(f'TOTAL {tot//1024} MB')
