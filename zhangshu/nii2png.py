import numpy as np
import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
count = 0

def nii_to_image(filepath, imgfile):
    global count
    filenames = os.listdir(filepath)  # 读取nii文件夹
    print(filenames)

    for f in filenames:
        # 开始读取nii文件
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)  # 读取nii
        img_fdata = img.get_fdata()
        # 开始转换为图像
        (x, y, z) = img.shape
        print(x,y,z)
        for i in range(z):  # z是图像的序列
            silce = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
            imageio.imwrite(os.path.join(imgfile, '{}.png'.format(count)), silce)
            count = count + 1


if __name__ == '__main__':
    filepath = 'E:/pythondemo/lobeseg/data/preoperotive/test/mask/'
    imgfile = "E:/pythondemo/lobeseg/data/preoperotive/test/mask2png/"
    nii_to_image(filepath, imgfile)