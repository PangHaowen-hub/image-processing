import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt


def transposeMask(ct_path, mask_path):
    # ct_sitk_img = sitk.ReadImage(mask_path)

    ct_reader = sitk.ImageSeriesReader()
    dicom_names = ct_reader.GetGDCMSeriesFileNames(ct_path)
    ct_reader.SetFileNames(dicom_names)
    ct_sitk_img = ct_reader.Execute()
    ct_img_arr = sitk.GetArrayFromImage(ct_sitk_img)
    print(ct_img_arr.shape)
    print(ct_sitk_img.GetDirection())

    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    mask_img_arr = np.flip(mask_img_arr, axis=1)
    mask_img_arr = np.flip(mask_img_arr, axis=2)

    print(mask_img_arr.shape)
    print(mask_sitk_img.GetDirection())

    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(ct_sitk_img.GetDirection())
    new_mask_img.SetOrigin(ct_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(ct_sitk_img.GetSpacing())
    # new_file_path = r'D:\lung_label\label2'

    # writer = sitk.WriteImage(new_mask_img, os.path.join(new_file_path, 'R01123846_lobes_new.nii'))
    writer = sitk.WriteImage(new_mask_img, mask_path[0:-6] + '_transpose.nii.gz')


if __name__ == '__main__':
    ct_path = r'F:\lobe\lobe_data_lobe\LL_final\after\select_ct\chenyuxiang_after'
    mask_path = r'F:\my_lobe_data\after\LL\masks_rename\LL_000.nii.gz'
    transposeMask(ct_path, mask_path)
