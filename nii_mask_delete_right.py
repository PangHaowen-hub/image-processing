import SimpleITK as sitk
import numpy as np
import os

import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def delete_label(mask, save_path):
    mask1_img = sitk.ReadImage(mask)
    mask1_arr = sitk.GetArrayFromImage(mask1_img)
    temp = mask1_arr.copy()
    mask1_arr[temp > 3] = 0
    mask1_arr[temp == 2] = 1
    mask1_arr[temp == 3] = 2

    new_mask_img = sitk.GetImageFromArray(mask1_arr)
    new_mask_img.SetDirection(mask1_img.GetDirection())
    new_mask_img.SetSpacing(mask1_img.GetSpacing())
    new_mask_img.SetOrigin(mask1_img.GetOrigin())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    mask_path = r'G:\my_lobe_data\after\RU\masks_rename'
    save_path = r'G:\my_lobe_data\after\RU\delete_left_labe_mask'
    img_list = get_listdir(mask_path)
    for i in tqdm.tqdm(img_list):
        delete_label(i, save_path)
