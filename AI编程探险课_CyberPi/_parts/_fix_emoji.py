# -*- coding: utf-8 -*-
import io
p = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
s = io.open(p, 'r', encoding='utf-8').read()
old = '<span class="ce-ico">\xf0\x9f\x93\x9a</span>'
new = '<span class="ce-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></span>'
if old in s:
    s = s.replace(old, new, 1)
    io.open(p, 'w', encoding='utf-8').write(s)
    print("OK: replaced emoji with SVG")
else:
    print("emoji not found, checking...")
    if '\xf0\x9f\x93\x9a' in s:
        print("emoji exists but not in expected context")
    else:
        print("no emoji found at all")
