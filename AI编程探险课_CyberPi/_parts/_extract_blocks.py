# -*- coding: utf-8 -*-
import io, re

path = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
with io.open(path, 'r', encoding='utf-8') as f:
    src = f.read()

# 提取所有 blocks 数组内容（用非贪婪匹配到]）
blocks = re.findall(r'blocks:\[(.*?)\](?=,\s*\n\s*\w+:)', src, re.DOTALL)
all_blocks = {}
for b in blocks:
    items = re.findall(r'\["([^"]+)","([^"]+)"\]', b)
    for cat, name in items:
        if cat not in all_blocks:
            all_blocks[cat] = set()
        all_blocks[cat].add(name)

for cat in sorted(all_blocks.keys()):
    print(f"=== {cat} ===")
    for name in sorted(all_blocks[cat]):
        print(f"  - {name}")
total = sum(len(v) for v in all_blocks.values())
print(f"\n--- 共 {len(all_blocks)} 个分类，{total} 种积木 ---")
