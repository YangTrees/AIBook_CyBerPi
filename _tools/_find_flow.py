# -*- coding: utf-8 -*-
import io, re
p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()
for kw in ['本课统一实施流程', 'MBLOCK', 'CYBERPI', '添加设备', '实体触发', '真机验收', '分段搭建', '找到积木', '选择模式']:
    idx = [m.start() for m in re.finditer(re.escape(kw), s)]
    print(kw, '->', len(idx), '处', idx[:5])
