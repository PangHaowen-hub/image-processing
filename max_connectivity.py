import SimpleITK as sitk
import numpy as np
import os
from skimage import measure
from tqdm import trange
import os
from collections import Counter


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def connectivity(mask, save_path):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    # x1 = mask_img_arr == 1
    # x2 = mask_img_arr == 2
    # x3 = mask_img_arr == 3
    # x5 = mask_img_arr == 5
    #
    #
    # mask_img_arr[mask_img_arr != 4] = 0



    labels = measure.label(mask_img_arr)
    num = Counter(labels.flatten())
    temp = sorted(num.items(), key=lambda item: item[1], reverse=True)[1:6]
    labels[labels == temp[0][0]] = -1
    labels[labels == temp[1][0]] = -1
    labels[labels == temp[2][0]] = -1
    labels[labels == temp[3][0]] = -1
    labels[labels == temp[4][0]] = -1
    # labels[labels == 51] = -1

    mask_img_arr[labels != -1] = 0
    # mask_img_arr[x1] = 1
    # mask_img_arr[x2] = 2
    # mask_img_arr[x3] = 3
    # mask_img_arr[x5] = 5
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(mask_sitk_img.GetDirection())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    mask_path = r'G:\Lobectomy\shengjing\LLL_nii\LL_before_test_all_temp'
    save_path = r'G:\Lobectomy\shengjing\LLL_nii\LL_before_test_all_temp'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in trange(len(mask)):
        connectivity(mask[i], save_path)

    #
    # mask = r'G:\Lobectomy\shengjing\RLL_nii\RL_after_test_all_temp\RL_016.nii.gz'
    # save = r'G:\Lobectomy\shengjing\RLL_nii\RL_after_test_all_temp'
    # connectivity(mask, save)