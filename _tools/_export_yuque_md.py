# -*- coding: utf-8 -*-
"""语雀 markdown 导出接口抓取"""
import urllib.request, re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for slug in ['basic_cases', 'advanced_cases', 'kk0ycmcnep9q2ks8']:
    url = f'https://www.yuque.com/makeblock-help-center-zh/cyberpi/{slug}/markdown?plain=true&linebreak=false&anchor=false'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36',
        'Referer': 'https://www.yuque.com/'
    })
    try:
        md = urllib.request.urlopen(req, timeout=40, context=ctx).read().decode('utf-8', errors='ignore')
        print(slug, 'len:', len(md))
        out = fr'D:\PROJECTS\_AI\AIBook_CyberPi\_tools\yuque_{slug}.md'
        open(out, 'w', encoding='utf-8').write(md)
        # 统计图片
        imgs = re.findall(r'!\[[^\]]*\]\((https?://[^)]+)\)', md)
        print('  images:', len(imgs))
        # 打印前几行
        for line in md.splitlines()[:12]:
            print('  |', line[:100])
    except Exception as e:
        print(slug, 'ERR', e)
