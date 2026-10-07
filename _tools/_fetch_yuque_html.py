# -*- coding: utf-8 -*-
"""抓取语雀文档HTML源码，提取图片URL"""
import urllib.request, re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https://www.yuque.com/makeblock-help-center-zh/cyberpi/basic_cases'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36',
    'Referer': 'https://www.yuque.com/'
})
html = urllib.request.urlopen(req, timeout=30, context=ctx).read().decode('utf-8', errors='ignore')
print('HTML len:', len(html))
# 提取所有 nlark CDN 图片 URL
urls = sorted(set(re.findall(r'https?://cdn\.nlark\.com/[^"\'\s\\)<>]+', html)))
print('nlark urls:', len(urls))
for u in urls[:60]:
    print(u[:160])
# 查找 SSR 数据
m = re.search(r'__INITIAL_STATE__|initialState|window\.[A-Za-z_]+\s*=\s*\{', html)
print('state marker:', m.group(0) if m else None)
