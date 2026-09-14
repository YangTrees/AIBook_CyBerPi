# -*- coding: utf-8 -*-
import io

path = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
with io.open(path, 'r', encoding='utf-8') as f:
    src = f.read()

old_css = "/* 积木 */\n.blk-list{display:flex;flex-direction:column;gap:10px}"

new_css = """/* 积木 */
.blk-guide{display:flex;gap:16px;align-items:flex-start;background:linear-gradient(135deg,hsl(214 80% 97%),hsl(28 100% 97%));border:2px solid hsl(214 60% 88%);border-radius:16px;padding:18px 20px;margin-bottom:18px}
.blk-guide .bg-ico{width:44px;height:44px;border-radius:12px;background:var(--primary);color:#fff;display:grid;place-items:center;flex:none}
.blk-guide .bg-ico svg{width:24px;height:24px}
.blk-guide b{font-size:15px;color:var(--ink);display:block;margin-bottom:4px}
.blk-guide p{font-size:13px;color:var(--ink-2);line-height:1.7;margin:0}
.blk-cat-intro{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin-bottom:18px}
.bci-item{display:flex;gap:10px;align-items:flex-start;background:var(--accent);border-radius:12px;padding:12px 14px}
.bci-dot{width:12px;height:12px;border-radius:4px;flex:none;margin-top:3px}
.bci-item b{font-size:13px;color:var(--ink);display:block;margin-bottom:2px}
.bci-item p{font-size:11.5px;color:var(--ink-2);line-height:1.6;margin:0}
.blk-cards{display:flex;flex-direction:column;gap:12px;margin-bottom:14px}
.blk-card{background:#fff;border:1.5px solid var(--line);border-radius:14px;padding:14px 16px;box-shadow:var(--shadow-sm)}
.blk-card-top{display:flex;gap:12px;align-items:center;margin-bottom:10px;flex-wrap:wrap}
.blk-desc{font-size:13px;color:var(--ink-2);line-height:1.7;padding-left:10px;border-left:3px solid var(--primary-100);padding-top:4px;padding-bottom:4px}
.blk-list{display:flex;flex-direction:column;gap:10px}"""

if old_css in src:
    src = src.replace(old_css, new_css, 1)
    print("OK: CSS added")
else:
    print("FAIL: old_css not found")
    idx = src.find("/* 积木 */")
    if idx >= 0:
        print("found at", idx)
        print(repr(src[idx:idx+120]))

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(src)
print("DONE")
