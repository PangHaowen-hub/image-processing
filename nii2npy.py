import SimpleITK as sitk
import os
from PIL import Image
import numpy as np
from tqdm import trange


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def nii2npy_path(img, save_path):  # 所有图像同一个文件夹
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)

    _, fullflname = os.path.split(img)
    for i in trange(img_arr.shape[0]):
        temp = img_arr[i, :, :]
        temp[temp > 1024] = 1024
        temp[temp < -1024] = -1024
        np.save(os.path.join(save_path, fullflname + str(i).rjust(4, '0') + '.npy'), temp)


if __name__ == '__main__':
    img_path = r'H:\CT2CECT\registration\data\cect_a_lung_resample\test'
    save_path = r'F:\my_code\pix2pix-ct2cect\data\CT2CECT_NPY_Elastix_a_vessel\test\B'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        nii2npy_path(img_list[i], save_path)
