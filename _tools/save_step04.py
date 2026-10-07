import hashlib
from PIL import Image

src = r'C:\Users\YL\AppData\Local\Temp\gac-runtime\shot.png'
out = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\blocks\lesson-31\step-04.png'

with open(src, 'rb') as fh:
    h_src = hashlib.md5(fh.read()).hexdigest()
print('src md5', h_src[:12])

im = Image.open(src)
print('src size', im.size)
crop = im.crop((0, 0, min(1519, im.size[0]), im.size[1]))
crop.save(out, 'PNG')
with open(out, 'rb') as fh:
    h_out = hashlib.md5(fh.read()).hexdigest()
print('out md5', h_out[:12])

# 对比既有 step-03
s3 = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\blocks\lesson-31\step-03.png'
with open(s3, 'rb') as fh:
    h_s3 = hashlib.md5(fh.read()).hexdigest()
print('step03 md5', h_s3[:12], 'same_as_out:', h_s3 == h_out)
