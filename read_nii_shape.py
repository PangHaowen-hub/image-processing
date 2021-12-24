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
    l_mask_path = r'F:\data\Train_Masks_nii'
    img_path = r'F:\data\Train_nii'

    l_mask = get_listdir(l_mask_path)
    l_mask.sort()

    img = get_listdir(img_path)
    img.sort()
    shape = []
    Spacing = []
    for i in range(len(l_mask)):
        sitk_mask = sitk.ReadImage(l_mask[i])
        sitk_img = sitk.ReadImage(img[i])

        mask_arr = sitk.GetArrayFromImage(sitk_mask)
        img_arr = sitk.GetArrayFromImage(sitk_img)

        print(mask_arr.shape)
        print(img_arr.shape)

    #     shape.append(img_arr.shape)
    #     Spacing.append(sitk_img.GetSpacing())
    #     print(i)
    #     print(img_arr.shape)
    #     print(sitk_img.GetSpacing())
    # print(min(shape))
    # print(max(shape))
