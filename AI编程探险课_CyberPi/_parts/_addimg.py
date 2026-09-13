# -*- coding: utf-8 -*-
import io
p = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts\shell.html"
s = io.open(p, encoding="utf-8").read()

# 硬件页加横幅
old1 = '点击图中部件查看功能</span>\n      </div>\n      <div class="hw-hero">'
new1 = '点击图中部件查看功能</span>\n      </div>\n      <div class="page-banner"><img src="assets/hardware.jpg" alt="团团和点点探索CyberPi硬件"></div>\n      <div class="hw-hero">'
if old1 in s:
    s = s.replace(old1, new1)
    print("hardware banner added")
else:
    print("hardware pattern NOT found")

# 成长页加横幅
old2 = '<h2>我的成长档案</h2>\n        <span class="en">My Growth</span>\n      </div>\n      <div class="grow-hero">'
new2 = '<h2>我的成长档案</h2>\n        <span class="en">My Growth</span>\n      </div>\n      <div class="page-banner"><img src="assets/growth.jpg" alt="团团和点点的成长档案"></div>\n      <div class="grow-hero">'
if old2 in s:
    s = s.replace(old2, new2)
    print("growth banner added")
else:
    print("growth pattern NOT found")

io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("done, size:", len(s))
