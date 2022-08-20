from PIL import Image
import os

os.chdir(r'E:/pythondemo')
for filename in os.listdir(r'E:/lobeseg'):
    im = Image.open(filename)
    im = im.rotate(270, expand=True)
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im.save(os.path.join('E:/pythondemo/lobeseg/data/preoperotive/test/rotate', filename))
