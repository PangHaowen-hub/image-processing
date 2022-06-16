import SimpleITK as sitk
import os

import tqdm
from PIL import Image
import numpy as np
from tqdm import trange


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_nii(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def pngmask2nii(mask_path, image_nii_path, save_path):
    sitk_img = sitk.ReadImage(image_nii_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)

    mask_list = get_listdir(mask_path)
    mask_list.sort()
    new_mask = np.zeros_like(img_arr)
    for i in trange(len(mask_list)):
        image = Image.open(mask_list[i])
        new_mask[i, :, :] = image
    new_mask[new_mask != 0] = 1  # TODO: 修改label
    new_mask = sitk.GetImageFromArray(new_mask)
    new_mask.SetDirection(sitk_img.GetDirection())
    new_mask.SetSpacing(sitk_img.GetSpacing())
    new_mask.SetOrigin(sitk_img.GetOrigin())
    _, fullflname = os.path.split(image_nii_path)
    sitk.WriteImage(new_mask, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    image_nii_path = r'H:\CT2CECT\segmentation_test\ISICDM2021\CECT'
    mask_path = r'H:\CT2CECT\segmentation\ISICDM2021\train\vessel\CTA'
    save_path = r'H:\CT2CECT\segmentation_test\ISICDM2021\CECT_mask'
    image_nii_list = get_nii(image_nii_path)
    image_nii_list.sort()
    mask_list = os.listdir(mask_path)
    mask_list.sort()
    for i in tqdm.trange(len(image_nii_list)):
        pngmask2nii(os.path.join(mask_path, mask_list[i]), image_nii_list[i], save_path)
