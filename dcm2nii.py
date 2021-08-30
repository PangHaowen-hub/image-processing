import os
import numpy as np
import SimpleITK as sitk


def get_ct_file(ctdir):
    ctpath = []
    ctlist = os.listdir(ctdir)  # 列出文件夹下所有的目录与文件
    # 遍历该文件夹下的所有目录或者文件
    for ii in range(0, len(ctlist)):
        path = os.path.join(ctdir, ctlist[ii])
        ctpath.append(path)
    return ctpath


def dcm_nii(ct_path):
    # 读取CT图像
    ct_reader = sitk.ImageSeriesReader()
    dicom_names = ct_reader.GetGDCMSeriesFileNames(ct_path)
    ct_reader.SetFileNames(dicom_names)
    ct_sitk_img = ct_reader.Execute()
    ct_img_arr = sitk.GetArrayFromImage(ct_sitk_img)

    # 获取病人姓名
    path1 = os.path.split(os.path.realpath(ct_path))[1]
    patient_name = os.path.split(path1)[1]

    new_mask_img1 = sitk.GetImageFromArray(ct_img_arr)
    new_mask_img1.SetDirection(ct_sitk_img.GetDirection())
    new_mask_img1.SetOrigin(ct_sitk_img.GetOrigin())
    new_mask_img1.SetSpacing(ct_sitk_img.GetSpacing())
    new_file_path = r'D:\github_code\Airway-master\example_data\my_data'
    path = os.path.join(new_file_path, patient_name + '.nii.gz')
    sitk.WriteImage(new_mask_img1, path)


if __name__ == '__main__':

    # 原始数据，不能有中文
    ctdir = r'D:\github_code\Airway-master\example_data\my_data\airway'
    ct_path = get_ct_file(ctdir)

    for i in range(len(ct_path)):
        dcm_nii(ct_path[i])
        i = i + 1
        print(i)
