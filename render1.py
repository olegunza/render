from PIL import Image
import re

scr_x, scr_y = 900, 900
kof_scr_x = int(scr_x/33)
kof_scr_y = int(scr_y/33)
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
            x = int((float(x)+12) * kof_scr_x)
            y = scr_y - int((float(y)+2) * kof_scr_y)
            canvas_pixels[x,y] = color

img.show()


