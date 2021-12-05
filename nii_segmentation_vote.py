import SimpleITK as sitk
import os
import copy
import torch
import tqdm
import numpy as np
import monai


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(mask1, mask2, mask3, save_path):
    mask_sitk_img1 = sitk.ReadImage(mask1)
    mask_img_arr1 = sitk.GetArrayFromImage(mask_sitk_img1)
    mask_sitk_img2 = sitk.ReadImage(mask2)
    mask_img_arr2 = sitk.GetArrayFromImage(mask_sitk_img2)
    mask_sitk_img3 = sitk.ReadImage(mask3)
    mask_img_arr3 = sitk.GetArrayFromImage(mask_sitk_img3)
    mask_img_torch1 = torch.from_numpy(mask_img_arr1)
    mask_img_torch2 = torch.from_numpy(mask_img_arr2)
    mask_img_torch3 = torch.from_numpy(mask_img_arr3)
    mask_img_torch1 = mask_img_torch1.unsqueeze(0)
    mask_img_torch2 = mask_img_torch2.unsqueeze(0)
    mask_img_torch3 = mask_img_torch3.unsqueeze(0)

    Vote = monai.transforms.VoteEnsemble(num_classes=6)
    mask_arr = Vote((mask_img_torch1, mask_img_torch2, mask_img_torch3))
    mask_arr = torch.squeeze(mask_arr, 0).detach().numpy()
    new_mask_img = sitk.GetImageFromArray(mask_arr)
    new_mask_img.SetDirection(mask_sitk_img1.GetDirection())
    new_mask_img.SetOrigin(mask_sitk_img1.GetOrigin())
    new_mask_img.SetSpacing(mask_sitk_img1.GetSpacing())
    _, fullflname = os.path.split(mask1)
    sitk.WriteImage(new_mask_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    mask1_path = r'F:\my_code\ISICDM2021\pred\lungmask_pred\CT'
    mask2_path = r'F:\my_code\ISICDM2021\pred\nnunet_pred\CT'
    mask3_path = r'F:\my_code\ISICDM2021\pred\unet_pred\CT'
    save_path = r'F:\my_code\ISICDM2021\pred'

    mask_list1 = get_listdir(mask1_path)
    mask_list1.sort()
    mask_list2 = get_listdir(mask2_path)
    mask_list2.sort()
    mask_list3 = get_listdir(mask3_path)
    mask_list3.sort()
    for i in tqdm.trange(len(mask_list1)):
        add_label(mask_list1[i], mask_list2[i], mask_list3[i], save_path)
