from PIL import Image
import re

scr_x, scr_y = 800, 800
half_scr_x = int(scr_x/33)
half_scr_y = int(scr_y/33)
xlist = []
ylist = []
img = Image.new('RGB', (scr_x, scr_y), 'black')
canvas_pixels = img.load()
color = (255, 255, 255)
with open('Girl+Head.obj') as f:
    lines = f.read()
    for line in lines.split('\n'):
        try:
           v, x, y, z = re.split('\s*', line)
        except:
            continue
        if v == 'v':
            xlist.append(float(x))
            ylist.append(float(y))


print(max(xlist),min(xlist))
print(max(ylist),min(ylist))