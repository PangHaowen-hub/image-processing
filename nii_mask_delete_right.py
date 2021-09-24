import SimpleITK as sitk
import numpy as np
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def delete_label(mask1, mask2, save_path):
    mask1_img = sitk.ReadImage(mask1)
    mask1_arr = sitk.GetArrayFromImage(mask1_img)
    mask2_img = sitk.ReadImage(mask2)
    mask2_arr = sitk.GetArrayFromImage(mask2_img)
    mask1_arr[mask2_arr != 1] = 0
    new_mask_img = sitk.GetImageFromArray(mask1_arr)
    new_mask_img.SetDirection(mask1_img.GetDirection())
    new_mask_img.SetSpacing(mask1_img.GetSpacing())
    new_mask_img.SetOrigin(mask1_img.GetOrigin())
    sitk.WriteImage(new_mask_img, save_path)


if __name__ == '__main__':
    mask1_path = r'F:\segment_registration\segmentation\26_30\030\CT8_mask.nii.gz'
    mask2_path = r'F:\segment_registration\segmentation\26_30\030\CT8_lobe.nii.gz'
    save_path = r'F:\segment_registration\segmentation\26_30\030\CT8_mask_segments.nii.gz'
    delete_label(mask1_path, mask2_path, save_path)
