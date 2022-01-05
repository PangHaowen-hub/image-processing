import os
import numpy as np
import SimpleITK as sitk
from tqdm import trange


def get_ct_file(main_path):
    ctpath = []
    ct_list = os.listdir(main_path)  # 列出文件夹下所有的目录与文件
    # 遍历该文件夹下的所有目录或者文件
    for ii in range(0, len(ct_list)):
        path = os.path.join(main_path, ct_list[ii])
        ctpath.append(path)
    return ctpath


def dcm_nii(ct_path, save_path):
    # 读取CT图像
    ct_reader = sitk.ImageSeriesReader()
    dicom_names = ct_reader.GetGDCMSeriesFileNames(ct_path)
    ct_reader.SetFileNames(dicom_names)
    ct_sitk_img = ct_reader.Execute()
    ct_img_arr = sitk.GetArrayFromImage(ct_sitk_img)
    print(ct_img_arr.shape)

    # 获取病人姓名
    name = os.path.split(ct_path)[1]

    new_mask_img1 = sitk.GetImageFromArray(ct_img_arr)
    new_mask_img1.SetDirection(ct_sitk_img.GetDirection())
    new_mask_img1.SetOrigin(ct_sitk_img.GetOrigin())
    new_mask_img1.SetSpacing(ct_sitk_img.GetSpacing())
    path = os.path.join(save_path, name + '.nii.gz')
    sitk.WriteImage(new_mask_img1, path)


if __name__ == '__main__':

    # 原始数据，不能有中文
    main_path = r'C:\Users\user\Desktop\temp'
    save_path = r'I:\paper\1-lungCT\niifile\COPD\yxy'
    ct_path = get_ct_file(main_path)
    ct_path.sort()
    for i in trange(len(ct_path)):
        dcm_nii(ct_path[i], save_path)
