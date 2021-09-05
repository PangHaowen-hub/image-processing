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


def nii_raw(img1, img2, img3, lobe, save_path):
    sitk_img_1 = SimpleITK.ReadImage(img1)
    img_arr_1 = SimpleITK.GetArrayFromImage(sitk_img_1)
    sitk_img_2 = SimpleITK.ReadImage(img2)
    img_arr_2 = SimpleITK.GetArrayFromImage(sitk_img_2)
    sitk_img_3 = SimpleITK.ReadImage(img3)
    img_arr_3 = SimpleITK.GetArrayFromImage(sitk_img_3)
    sitk_img_lobe = SimpleITK.ReadImage(lobe)
    img_arr_lobe = SimpleITK.GetArrayFromImage(sitk_img_lobe)
    img_arr_1 = img_arr_1.astype(np.int16)
    # img_arr_1 = img_arr_1 / 255 * 1800 - 1200
    # img_arr_1 = img_arr_1 * 7 - 1200
    img_arr_1[img_arr_lobe == 1] = 100
    img_arr_1[img_arr_lobe == 2] = 200
    img_arr_1[img_arr_lobe == 3] = 300
    img_arr_1[img_arr_2 == 1] = 500
    img_arr_1[img_arr_2 == 2] = 700
    img_arr_1[img_arr_3 == 1] = 600

    new_mask_img = SimpleITK.GetImageFromArray(img_arr_1)
    new_mask_img.SetSpacing(sitk_img_1.GetSpacing())
    new_mask_img.SetOrigin(sitk_img_1.GetOrigin())
    new_mask_img.SetDirection(sitk_img_1.GetDirection())
    # _, fullflname = os.path.split(img1)
    SimpleITK.WriteImage(new_mask_img, save_path)


if __name__ == '__main__':
    img_1_path = r'F:\segment_registration\segmentation\26_30\026\CT3_clean_hu.nii.gz'
    img_2_path = r'F:\segment_registration\segmentation\26_30\026\CT3_av.nii.gz'
    img_3_path = r'F:\segment_registration\segmentation\26_30\026\CT3_airway.nii.gz'
    lobe_path = r'F:\segment_registration\segmentation\26_30\026\CT3_lobe_mask.nii.gz'


    save_path = r'F:\segment_registration\segmentation\26_30\026\CT3_av.mhd'
    nii_raw(img_1_path, img_2_path, img_3_path, lobe_path, save_path)

    # img_1_path = r'F:\segment_registration\segmentation\26_30\026\CT3.nii.gz'
    # img_2_path = r'F:\segment_registration\segmentation\26_30\026\CT3_av.nii.gz'
    # img_3_path = r'F:\segment_registration\segmentation\26_30\026\CT3_airway.nii.gz'
    # save_path = r'F:\segment_registration\segmentation\26_30\026\CT3_av.mhd'
    # nii_raw(img_1_path, img_2_path, img_3_path, save_path)
