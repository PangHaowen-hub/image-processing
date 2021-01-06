import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read(Filelist_CT, Filelist_mask):
    # 读取dicom
    # ct_reader = sitk.ImageSeriesReader()
    # dicom_names = ct_reader.GetGDCMSeriesFileNames(Filelist_CT)
    # ct_reader.SetFileNames(dicom_names)
    # ct_sitk_img = ct_reader.Execute()
    # ct_img_arr = sitk.GetArrayFromImage(ct_sitk_img)
    # print(ct_img_arr.shape)

    # alignedCT_sitk_img = sitk.ReadImage(Filelist_CT)
    # alignedCT_img_arr = sitk.GetArrayFromImage(alignedCT_sitk_img)
    # print(alignedCT_img_arr.shape)

    # 读取mask
    mask_sitk_img = sitk.ReadImage(Filelist_mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    # print(mask_img_arr.shape)


    height, long, width = mask_img_arr.shape

    # 计算肺的最高点和最低点
    n1, n2, n3 = np.where(mask_img_arr ==1)
    # print(n1,n2,n3)
    a = n1[0]
    b = n1[-1]
    high=int(abs(a-b))
    c=n2[0]
    d=n2[-1]
    long=int(abs(c-d))
    e=n3[0]
    f=n3[-1]
    wide=int(abs(e-f))
    print(wide)

# dicom
# def get_filelist1(path_CT):
#     Filelist_CT = []
#     for home, dirs, files_CT in os.walk(path_CT):
#         for dir in dirs:
#             Filelist_CT.append(os.path.join(home, dir))
#         return Filelist_CT

# nii
def get_filelist1(path_CT):
    Filelist_CT = []
    for home, dirs, files_CT in os.walk(path_CT):
        for filename in files_CT:
            Filelist_CT.append(os.path.join(home, filename))
        return Filelist_CT

def get_filelist2(path_mask):
     Filelist_mask = []
     for home, dirs, files_mask in os.walk(path_mask):
          for filename in files_mask:
              Filelist_mask.append(os.path.join(home, filename))
          return Filelist_mask

if __name__ == '__main__':
    path_CT = r'E:/90data/RL_final/GU_before/gu_ct/'
    path_mask =r'E:/90data/RL_final/GU_before/gu_mask/'
    Filelist_CT = get_filelist1(path_CT)
    print(Filelist_CT)
    print(len(Filelist_CT))

    Filelist_mask = get_filelist2(path_mask)
    print(Filelist_mask)
    print(len(Filelist_mask))
    file = len(Filelist_mask)

    for i in range(file):
        read(Filelist_CT[i], Filelist_mask[i])

