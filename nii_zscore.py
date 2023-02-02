import numpy as np
import os
import SimpleITK as sitk
import tqdm


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def normalization(img_path, save_path):
    sitk_img = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    new_arr = (img_arr - np.mean(img_arr)) / np.std(img_arr)
    new_img = sitk.GetImageFromArray(new_arr)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetOrigin(sitk_img.GetOrigin())
    new_img.SetSpacing(sitk_img.GetSpacing())
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    img_path = r'F:\my_code\bit_pgan\pGAN_nii_input\data_test\train\20210416_ZHOUBING_055_F_p620'
    save_path = r'F:\my_code\bit_pgan\pGAN_nii_input\data_test\train\20210416_ZHOUBING_055_F_p620'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in tqdm.tqdm(img_list):
        normalization(i, save_path)
