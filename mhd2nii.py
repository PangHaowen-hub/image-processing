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


def raw2nii(img, save_path):
    itkimage = sitk.ReadImage(img)  # 读取.mhd文件
    _, fullflname = os.path.split(img)
    sitk.WriteImage(itkimage, os.path.join(save_path, fullflname[:-4] + '.nii.gz'))


if __name__ == '__main__':
    img_path = r'G:\dir-lab\copd\copd1'
    save_path = r'G:\dir-lab\copd\copd1'
    img_list = get_listdir(img_path)
    for i in tqdm.tqdm(img_list):
        raw2nii(img_path, save_path)

