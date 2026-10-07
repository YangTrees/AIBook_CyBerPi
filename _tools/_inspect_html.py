# -*- coding: utf-8 -*-
import io, re
s = io.open(r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html', encoding='utf-8').read()
idx = [m.start() for m in re.finditer(r'title', s)]
print('total title count:', len(idx))
for i in idx[:10]:
    print(repr(s[i-60:i+80]))
    print('---')
