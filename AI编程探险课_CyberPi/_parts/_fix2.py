import io, re, glob
for f in glob.glob(r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts\data*.js"):
    s = io.open(f, encoding='utf-8').read()
    def fix(m):
        lid = int(m.group(1))
        return "id:%d, ch:%d" % (lid, (lid + 7) // 8)
    s2 = re.sub(r"id:(\d+),\s*ch:\d+", fix, s)
    io.open(f, 'w', encoding='utf-8').write(s2)
    print(f, "->", re.findall(r"id:(\d+),\s*ch:(\d+)", s2))
