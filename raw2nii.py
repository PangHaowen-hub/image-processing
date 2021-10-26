import SimpleITK as sitk
import numpy as np
import os

import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.mhd':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def delete_label(img, save_path):
    itkimage = sitk.ReadImage(img)  # 读取.mhd文件
    _, fullflname = os.path.split(img)
    sitk.WriteImage(itkimage, os.path.join(save_path, fullflname[:-4] + '.nii.gz'))


if __name__ == '__main__':
    img_path = r'G:\EMPIRE10\lung_mask'
    save_path = r'G:\EMPIRE10\lung_mask_nii'
    img_list = get_listdir(img_path)
    for i in tqdm.tqdm(img_list):
        delete_label(i, save_path)

