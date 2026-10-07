import sys
from PIL import Image

src = r'C:\Users\YL\AppData\Local\Temp\gac-runtime\shot.png'
out = sys.argv[1] if len(sys.argv) > 1 else r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\blocks\lesson-31\step-03.png'
im = Image.open(src)
w, h = im.size
crop_w = min(1519, w)
crop = im.crop((0, 0, crop_w, h))
crop.save(out, 'PNG')
print('saved', out, crop.size)
