import SimpleITK as sitk
import os
import tqdm
import numpy as np
import copy


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def volume(img, mask, save_path):
    img_sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(img_sitk_img)
    mask_sitk_img = sitk.ReadImage(mask)
    mask_arr = sitk.GetArrayFromImage(mask_sitk_img)

    save_arr = np.zeros_like(img_arr)
    save_arr[img_arr < -951] = 1  # 低密度
    temp = np.zeros_like(img_arr)
    temp[img_arr > -950] += 1
    temp[img_arr < -701] += 1
    save_arr[temp == 2] = 2  # 中密度
    save_arr[img_arr > -700] = 3  # 高密度

    lobe1 = copy.deepcopy(save_arr)
    lobe1[mask_arr != 1] = 0
    lobe2 = copy.deepcopy(save_arr)
    lobe2[mask_arr != 2] = 0
    lobe3 = copy.deepcopy(save_arr)
    lobe3[mask_arr != 3] = 0
    lobe4 = copy.deepcopy(save_arr)
    lobe4[mask_arr != 4] = 0
    lobe5 = copy.deepcopy(save_arr)
    lobe5[mask_arr != 5] = 0

    _, fullflname = os.path.split(img)

    new_lobe1 = sitk.GetImageFromArray(lobe1)
    new_lobe1.SetDirection(img_sitk_img.GetDirection())
    new_lobe1.SetOrigin(img_sitk_img.GetOrigin())
    new_lobe1.SetSpacing(img_sitk_img.GetSpacing())
    sitk.WriteImage(new_lobe1, os.path.join(save_path, 'lobe1' + fullflname))

    new_lobe2 = sitk.GetImageFromArray(lobe1)
    new_lobe2.SetDirection(img_sitk_img.GetDirection())
    new_lobe2.SetOrigin(img_sitk_img.GetOrigin())
    new_lobe2.SetSpacing(img_sitk_img.GetSpacing())
    sitk.WriteImage(new_lobe2, os.path.join(save_path, 'lobe2' + fullflname))

    new_lobe3 = sitk.GetImageFromArray(lobe1)
    new_lobe3.SetDirection(img_sitk_img.GetDirection())
    new_lobe3.SetOrigin(img_sitk_img.GetOrigin())
    new_lobe3.SetSpacing(img_sitk_img.GetSpacing())
    sitk.WriteImage(new_lobe3, os.path.join(save_path, 'lobe3' + fullflname))

    new_lobe4 = sitk.GetImageFromArray(lobe1)
    new_lobe4.SetDirection(img_sitk_img.GetDirection())
    new_lobe4.SetOrigin(img_sitk_img.GetOrigin())
    new_lobe4.SetSpacing(img_sitk_img.GetSpacing())
    sitk.WriteImage(new_lobe4, os.path.join(save_path, 'lobe4' + fullflname))

    new_lobe5 = sitk.GetImageFromArray(lobe1)
    new_lobe5.SetDirection(img_sitk_img.GetDirection())
    new_lobe5.SetOrigin(img_sitk_img.GetOrigin())
    new_lobe5.SetSpacing(img_sitk_img.GetSpacing())
    sitk.WriteImage(new_lobe5, os.path.join(save_path, 'lobe5' + fullflname))


if __name__ == '__main__':
    img_path = r'G:\Lobectomy\dalian\LLL\before\img_nii'
    mask_path = r'G:\Lobectomy\dalian\LLL\before\mask'
    save_path = r'G:\Lobectomy\dalian\LLL\before'
    img_list = get_listdir(img_path)
    mask_list = get_listdir(mask_path)
    img_list.sort()
    mask_list.sort()

    for i in tqdm.trange(len(img_list)):
        volume(img_list[i], mask_list[i], save_path)
