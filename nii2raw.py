import SimpleITK
import os
import numpy as np


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def nii_raw(img1, save_path):
    sitk_img_1 = SimpleITK.ReadImage(img1)
    SimpleITK.WriteImage(sitk_img_1, save_path)


if __name__ == '__main__':
    img_1_path = r'H:\CT2CECT\pix2pix\data\ncct\001.nii.gz'
    save_path = r'H:\ix\ncct_001.mhd'
    nii_raw(img_1_path, save_path)

