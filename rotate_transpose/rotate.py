from PIL import Image
import os
#'D:\\test\\test4\\'可以替换成图片文件所在的路径。
os.chdir('E:\\pythondemo\\lobeseg\\data\\preoperotive\\test\\mask2png')
for filename in os.listdir('E:\\pythondemo\\lobeseg\\data\\preoperotive\\test\\mask2png\\'):
    #print(filename)
    im=Image.open(filename)
    im=im.rotate(270,expand=True)
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
#在图片文件夹中手动新建一个名为rotated的文件夹，用于存储旋转后的图片
    im.save(os.path.join('E:/pythondemo/lobeseg/data/preoperotive/test/rotate',filename))
