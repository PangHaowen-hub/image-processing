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


if __name__ == '__main__':

    # 原始数据
    ctdir = r'F:\Double_gas_phase_syyxy\1\31200119009\1.2.840.113619.2.428.3.2831197974.665.1579215829.363'
    ct_path = get_ct_file(ctdir)

    for i in range(len(ct_path)):
        dcm_nii(ct_path[i])
        i = i + 1
        print(i)
