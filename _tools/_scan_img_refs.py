# -*- coding: utf-8 -*-
"""Extract per-lesson image references from index.html to find placeholders."""
import re, json

p = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
html = open(p, encoding='utf-8').read()

# Find LESSONS array image-related fields: img, gif, stepGif, media, programImg, answerImg etc
# Approach: extract each lesson object (id:..) and the following ~60 lines, collect asset paths.
# Simpler: collect all unique asset references used in <img> or in JS strings with assets/
paths = set(re.findall(r'assets/(?:blocks|yuque_web|yuque_steps|media|img)[^"\')\s]*', html))
print("=== ALL unique asset refs (count %d) ===" % len(paths))
by_cat = {}
for x in sorted(paths):
    cat = x.split('/')[1]
    by_cat.setdefault(cat, []).append(x)
for c in sorted(by_cat):
    print(f"\n--- {c} ({len(by_cat[c])}) ---")
    for x in by_cat[c][:80]:
        print("  " + x)
