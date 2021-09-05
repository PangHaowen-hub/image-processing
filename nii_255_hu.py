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


def nii_255_hu(img1, save_path):
    sitk_img_1 = SimpleITK.ReadImage(img1)
    img_arr_1 = SimpleITK.GetArrayFromImage(sitk_img_1)
    img_arr_1 = img_arr_1.astype(np.int16)
    # img_arr_1 = img_arr_1 / 255 * 1800 - 1200
    img_arr_1 = img_arr_1 * 7 - 1200

    new_mask_img = SimpleITK.GetImageFromArray(img_arr_1)
    new_mask_img.SetSpacing(sitk_img_1.GetSpacing())
    new_mask_img.SetOrigin(sitk_img_1.GetOrigin())
    new_mask_img.SetDirection(sitk_img_1.GetDirection())
    # _, fullflname = os.path.split(img1)
    SimpleITK.WriteImage(new_mask_img, save_path)


if __name__ == '__main__':
    img_1_path = r'F:\segment_registration\segmentation\26_30\026\CT3_clean_hu.nii.gz'
    save_path = r'F:\segment_registration\segmentation\26_30\026\CT3_hu.nii.gz'
    nii_255_hu(img_1_path, save_path)
