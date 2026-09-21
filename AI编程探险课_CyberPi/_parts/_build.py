import io, os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parts = os.path.join(base, "_parts")

head = io.open(os.path.join(parts, "head.html"), encoding="utf-8").read()
shell = io.open(os.path.join(parts, "shell.html"), encoding="utf-8").read()
data = ""
for f in ["data1.js", "data2.js", "data3.js", "data4.js", "refinements.js"]:
    data += io.open(os.path.join(parts, f), encoding="utf-8").read() + "\n"
app = io.open(os.path.join(parts, "app.js"), encoding="utf-8").read()

script_block = "<script>\n/* ===== 课程数据 ===== */\n" + data + "\n/* ===== 应用逻辑 ===== */\n" + app + "\n</script>"
out = shell.replace("</body>", script_block + "\n</body>")
out = head + out

dest = os.path.join(base, "index.html")
io.open(dest, "w", encoding="utf-8").write(out)
print("assembled:", dest, len(out), "chars")
