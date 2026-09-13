import io
p = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts\data1.js"
s = io.open(p, encoding='utf-8').read()
for n in range(2, 9):
    s = s.replace("ch:%d," % n, "ch:1,")
io.open(p, 'w', encoding='utf-8').write(s)
print("fixed:", s.count("ch:1,"))
