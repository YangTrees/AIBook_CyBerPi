import os, hashlib, json
from PIL import Image

root = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\blocks'
report = {}
for d in sorted(os.listdir(root)):
    p = os.path.join(root, d)
    if not os.path.isdir(p) or not d.startswith('lesson-'):
        continue
    files = {}
    for f in sorted(os.listdir(p)):
        fp = os.path.join(p, f)
        if not os.path.isfile(fp):
            continue
        size = os.path.getsize(fp)
        with open(fp, 'rb') as fh:
            h = hashlib.md5(fh.read()).hexdigest()[:10]
        files[f] = {'size': size, 'md5': h}
    report[d] = files

# 输出: 每个课程的文件 + 同md5分组
for d in sorted(report):
    files = report[d]
    by_md5 = {}
    for f, info in files.items():
        by_md5.setdefault(info['md5'], []).append(f)
    dup = {k: v for k, v in by_md5.items() if len(v) > 1}
    line = d
    parts = []
    for f in sorted(files):
        parts.append(f'{f}={files[f]["size"]}')
    flag = ''
    if dup:
        flag = ' DUP:' + ';'.join(','.join(v) for v in dup.values())
    print(d, ' | '.join(parts), flag)
