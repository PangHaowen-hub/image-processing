import SimpleITK as sitk
import os

import numpy as np


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'H:\my_lobe_data\lobectomy_classification\train_test_mask\0'

    img = get_listdir(img_path)
    img.sort()
    shape = []
    Spacing = []
    for i in range(len(img)):
        sitk_img = sitk.ReadImage(img[i])
        img_arr = sitk.GetArrayFromImage(sitk_img)
        print(img_arr.shape)
        shape.append(img_arr.shape)
        Spacing.append(sitk_img.GetSpacing())
        # print(sitk_img.GetSpacing())
    print(min(shape))
    print(max(shape))