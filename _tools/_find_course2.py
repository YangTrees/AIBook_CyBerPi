# -*- coding: utf-8 -*-
import io, re
s = io.open(r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html', encoding='utf-8').read()
# 课程数据结构可能形如 {id:2, title:...} 或 id:"2"
for m in re.finditer(r'id\s*:\s*["\x27]?(\d+)["\x27]?\s*,\s*title\s*:\s*["\x27]([^"\x27]+)["\x27]', s):
    print(m.group(1), '|', m.group(2))
