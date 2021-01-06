import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read(Filelist_CT, Filelist_mask):
    # 读取dicom
    ct_reader = sitk.ImageSeriesReader()
    dicom_names = ct_reader.GetGDCMSeriesFileNames(Filelist_CT)
    ct_reader.SetFileNames(dicom_names)
    ct_sitk_img = ct_reader.Execute()
    ct_img_arr = sitk.GetArrayFromImage(ct_sitk_img)
    # print(ct_img_arr.shape)

    # 读取mask
    mask_sitk_img = sitk.ReadImage(Filelist_mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    # print(mask_img_arr.shape)

    # 读取alignedct和alignedmask
    # alignedCT_sitk_img = sitk.ReadImage(Filelist_CT)
    # alignedCT_img_arr = sitk.GetArrayFromImage(alignedCT_sitk_img)
    # print(alignedCT_img_arr.shape)



    mask_img_arr = ct_img_arr * np.where(mask_img_arr ==3, 1, 0)
    # mask_img_arr = alignedCT_img_arr * np.where(mask_img_arr == 5, 1, 0)


    arr = mask_img_arr.ravel()

    plt.figure()

    n, bins, patches = plt.hist(arr, density=True, bins=9, range=[-1000, -100])
    print(n)



    plt.ylim(0, 0.01)  # Y轴范围
    # plt.xlabel("LL_pixel")
    picture_name = Filelist_CT.split('/')[-1] + '_LL'
    print(picture_name)

    # return n


def get_filelist1(path_CT):
    Filelist_CT = []
    for home, dirs, files_CT in os.walk(path_CT):
        for dir in dirs:
            Filelist_CT.append(os.path.join(home, dir))
        return Filelist_CT
# def get_filelist1(path_CT):
#     Filelist_CT = []
#     for home, dirs, files_CT in os.walk(path_CT):
#         for filename in files_CT:
#             Filelist_CT.append(os.path.join(home, filename))
#         return Filelist_CT
def get_filelist2(path_mask):
     Filelist_mask = []
     for home, dirs, files_mask in os.walk(path_mask):
          for filename in files_mask:
              Filelist_mask.append(os.path.join(home, filename))
          return Filelist_mask



if __name__ == '__main__':
    path_CT = r'E:/90data/LL_final/before/select_ct/'
    path_mask =r'E:/90data/LL_final/before/mask/'
    Filelist_CT = get_filelist1(path_CT)
    # print(Filelist_CT)
    # print(len(Filelist_CT))

    Filelist_mask = get_filelist2(path_mask)
    # print(Filelist_mask)
    # print(len(Filelist_mask))
    file = len(Filelist_mask)


    list = []
    for i in range(file):
        n = read(Filelist_CT[i], Filelist_mask[i])
        list.append(n)
    pd_data = pd.DataFrame(list)

    pd_data.to_csv('E:\zhang.csv')



