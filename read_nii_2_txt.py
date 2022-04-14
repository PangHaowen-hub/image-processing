import SimpleITK as sitk
import os

import numpy as np


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            tmp_list.append(file[:-9])
    return tmp_list


if __name__ == '__main__':
    img_path = r'G:\gz_data\double_gas\image_580_nii\i'
    save_path = r'G:\gz_data\double_gas\image_580_nii\i.txt'
    path_list = get_listdir(img_path)
    path_list.sort()
    for file_name in path_list:
        # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
        with open(save_path, "a") as file:
            file.write(file_name + "\n")
            print(file_name)
        file.close()
