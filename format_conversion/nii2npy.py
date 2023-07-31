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
    for i in range(img_arr.shape[0]):
        temp = img_arr[i, :, :]
        temp[temp > 0] = 0
        temp[temp < -1000] = -1000
        np.save(os.path.join(save_path, fullflname + str(i).rjust(4, '0') + '.npy'), temp)


if __name__ == '__main__':
    img_path = r'H:\PRM\59_cases_nii\59_cases_nii_e_lung'
    save_path = r'F:\my_code\copd_PRM\CycleResViT-PRM\datasets\PRM_npy'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        nii2npy_path(img_list[i], save_path)
