import torch
import torchio as tio
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

    img_arr = np.expand_dims(img_arr, axis=0)
    normalization_transform = tio.transforms.RescaleIntensity(out_min_max=(0, 1))
    new_arr = normalization_transform(img_arr)
    new_arr = np.squeeze(new_arr, 0)
    new_img = sitk.GetImageFromArray(new_arr)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetOrigin(sitk_img.GetOrigin())
    new_img.SetSpacing(sitk_img.GetSpacing())
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    img_path = r'G:\CT2CECT\registration\moving_v_resample_norm'
    save_path = r'G:\CT2CECT\registration\moving_v_resample_norm'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in tqdm.tqdm(img_list):
        normalization(i, save_path)
