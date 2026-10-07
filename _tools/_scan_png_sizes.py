# -*- coding: utf-8 -*-
"""Scan block screenshot PNG sizes to identify placeholders vs real screenshots."""
import os, struct
from collections import defaultdict

root = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\blocks"

def png_size(path):
    with open(path, 'rb') as f:
        head = f.read(33)
    if head[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    w, h = struct.unpack('>II', head[16:24])
    return (w, h)

sizes = defaultdict(list)
errs = []
for dirpath, dirnames, filenames in os.walk(root):
    for fn in sorted(filenames):
        if fn.lower().endswith('.png'):
            p = os.path.join(dirpath, fn)
            sz = png_size(p)
            d = os.path.basename(dirpath)
            if sz is None:
                errs.append(os.path.join(d, fn))
            else:
                sizes[sz].append(os.path.join(d, fn))

print("=== SIZES ===")
for sz in sorted(sizes, key=lambda s: (s[1], s[0])):
    print(f"{sz[0]}x{sz[1]} : {len(sizes[sz])} files")
    print("   " + ", ".join(sizes[sz][:12]))

print("\n=== ERRORS ===")
for e in errs[:30]:
    print(e)
