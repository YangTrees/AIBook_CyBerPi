# -*- coding: utf-8 -*-
"""Per-lesson asset reference audit: which images does index.html use per lesson, and do files exist?"""
import re, os, json

base = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi"
p = os.path.join(base, "index.html")
html = open(p, encoding='utf-8').read()

# All asset path occurrences (literal)
refs = re.findall(r'assets/(?:blocks|yuque_web|yuque_steps|media|img)/[^"\')\s,]+', html)

# Dynamic patterns: yuque_web/lesson-${n}.gif style concatenations
dyn = re.findall(r'assets/yuque_web/lesson-\$\{[^}]+\}\.gif', html)
dyn2 = re.findall(r"assets/yuque_web/lesson-'?\s*\+", html)

print("literal refs:", len(refs), "| dynamic yuque_web refs:", len(dyn), len(dyn2))

# Group literal refs by lesson
from collections import defaultdict
by_lesson = defaultdict(list)
misc = []
for r in refs:
    m = re.search(r'lesson-(\d+)', r)
    if m:
        by_lesson[int(m.group(1))].append(r)
    else:
        misc.append(r)

print("\n=== MISC (no lesson) ===")
for x in sorted(set(misc)):
    print("  ", x)

print("\n=== PER LESSON ===")
for i in range(1, 33):
    lst = sorted(set(by_lesson.get(i, [])))
    missing = []
    for x in lst:
        fp = os.path.join(base, x.replace('/', os.sep))
        if not os.path.exists(fp):
            missing.append(x)
    status = "OK" if not missing else "MISSING: " + "; ".join(missing)
    print(f"L{i:02d} ({len(lst)}): {status}")
    for x in lst:
        print("     " + x)
