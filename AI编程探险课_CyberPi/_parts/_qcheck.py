import io, glob

parts = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\_parts"
targets = ["data1.js", "data2.js", "data3.js", "data4.js"]
for fn in targets:
    s = io.open(parts + "\\" + fn, encoding="utf-8").read()
    print(fn, {
        "ascii_quote": s.count('"'),
        "left_cn_quote": s.count("\u201c"),
        "right_cn_quote": s.count("\u201d"),
        "corner": s.count("\u300c") + s.count("\u300d"),
    })
