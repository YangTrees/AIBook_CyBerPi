# -*- coding: utf-8 -*-
"""项目检查：index.html 资源引用完整性 + 可疑残留扫描"""
import io, os, re, glob

ROOT = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi'
HTML = os.path.join(ROOT, 'index.html')
s = io.open(HTML, encoding='utf-8').read()

# ---- 1. 资源引用完整性 ----
refs = set(re.findall(r'(?:src|href|url\(|background-image\s*:\s*url)\(?["\']?((?:\.\./)?assets/[^"\')\s]+)["\']?\)?', s))
refs |= set(re.findall(r'["\'](\.\./assets/[^"\']+)["\']', s))
missing = []
for r in sorted(refs):
    path = r.replace('../', '') if r.startswith('../') else r
    full = os.path.join(ROOT, path.replace('\\', '/').split('/')[0], *path.split('/')[1:]) if '/' in path else os.path.join(ROOT, path)
    if not os.path.exists(full):
        missing.append(r)
print('=== 资源引用检查 ===')
print('引用总数(去重):', len(refs))
print('缺失:', len(missing))
for m in missing[:40]:
    print('  MISSING:', m)

# ---- 2. Scratch / mBlock 对齐残留扫描 ----
print('\n=== 可疑残留扫描 ===')
patterns = {
    '小绿旗': ['小绿旗', '绿旗', '当 被点击', 'green flag', 'greenflag'],
    '舞台角色': ['舞台', '角色', '小猫', 'Scratch', 'scratch'],
    '非mBlock积木': ['当绿旗', '面向', '移动 10 步', '说.*(?:你好|hello)'],
}
for label, kws in patterns.items():
    hits = []
    for kw in kws:
        for m in re.finditer(re.escape(kw), s):
            line = s.count('\n', 0, m.start()) + 1
            ctx = s[max(0, m.start()-18):m.end()+18].replace('\n', ' ')
            hits.append((line, ctx))
    print(label, '->', len(hits), '处')
    for line, ctx in hits[:12]:
        print('   L%d: ...%s...' % (line, ctx))

# ---- 3. 课程数据结构 ----
print('\n=== 课程数据 ===')
for pat in ['var LESSONS =', 'var SAMPLE_CONTENT =', 'var OFFICIAL_STEPS =', 'var LESSON_META =', 'var BLOCKS_', 'function renderCourse', 'taskSpec']:
    n = s.count(pat)
    print(pat, '->', n)
# 每课 blocks 引用（assets/blocks/lesson-XX/step-02.png 等）
blk = set(re.findall(r'assets/blocks/lesson-\d+/[^"\']+', s))
print('blocks 引用数(去重):', len(blk))
# lessons 引用
les = set(re.findall(r'assets/lessons/[^"\']+', s))
print('lessons 引用数(去重):', len(les))
# official 引用
off = set(re.findall(r'assets/official/[^"\']+', s))
print('official 引用数(去重):', len(off))
# yuque_web 引用
yw = set(re.findall(r'assets/yuque_web/[^"\']+', s))
print('yuque_web 引用数(去重):', len(yw))
# yuque_steps 引用
ys = set(re.findall(r'assets/yuque_steps/[^"\']+', s))
print('yuque_steps 引用数(去重):', len(ys))
