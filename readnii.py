import numpy as np
import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像

count = 0
filepath = 'F:/lobe/all_CT_nii/Aligned_CT'
filenames = os.listdir(filepath)  # 读取nii文件夹
print(filenames)

for f in filenames:
    # 开始读取nii文件
    img_path = os.path.join(filepath, f)
    img = nib.load(img_path)  # 读取nii
    img_fdata = img.get_fdata()
    print(img_fdata)
    (x, y, z) = img.shape
    print(x, y, z)
