# -*- coding: utf-8 -*-
"""
更新网站index.html中32课SAMPLE_CONTENT的stepTitles
使其与修正后的课程步骤精确匹配
"""
import json, re

html_path = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
fixed_path = r"D:\PROJECTS\_AI\AIBook_CyberPi\_tools\_lessons_data_fixed.json"

# 读取修正后的课程数据
with open(fixed_path, encoding='utf-8') as f:
    lessons_fixed = json.load(f)

# 读取HTML
with open(html_path, encoding='utf-8') as f:
    content = f.read()

# 为每课更新stepTitles
updated = 0
for lid_str in sorted(lessons_fixed.keys(), key=int):
    lid = int(lid_str)
    data = lessons_fixed[lid_str]
    new_titles = data['stepTitles']
    
    # 构建新的stepTitles JS数组
    titles_js = '[' + ', '.join([f'"{t}"' for t in new_titles]) + ']'
    
    # 匹配该课的stepTitles字段
    # 模式：  N:{ ... stepTitles:[...], ...
    pattern = rf'({lid}:\{{[^}}]*?stepTitles:)\[[^\]]*\]'
    replacement = rf'\g<1>{titles_js}'
    
    new_content, n = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if n > 0:
        content = new_content
        updated += 1
        print(f"✓ 第{lid:2d}课 stepTitles已更新")
    else:
        print(f"✗ 第{lid}课 未找到stepTitles")

# 保存
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n完成！共更新 {updated} 课的stepTitles")

# 验证语法
import subprocess
result = subprocess.run(['node', '--check', html_path], capture_output=True, text=True)
if result.returncode == 0:
    print("✓ HTML中JavaScript语法检查通过")
else:
    print("✗ 语法错误:")
    print(result.stderr[:500])
