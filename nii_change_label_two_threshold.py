import SimpleITK as sitk
import os
import numpy as np
import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def change_label(img_i, img_e, save_path):
    sitk_img_i = sitk.ReadImage(img_i)
    i_img_arr = sitk.GetArrayFromImage(sitk_img_i)
    sitk_img_e = sitk.ReadImage(img_e)
    e_img_arr = sitk.GetArrayFromImage(sitk_img_e)

    temp = np.zeros_like(i_img_arr)

    temp[(i_img_arr >= -950) & (e_img_arr >= -856)] = 1
    temp[(i_img_arr >= -950) & (e_img_arr < -856)] = 2
    temp[(i_img_arr < -950) & (e_img_arr >= -856)] = 3
    temp[(i_img_arr < -950) & (e_img_arr < -856)] = 4

    new_img = sitk.GetImageFromArray(temp)
    new_img.SetDirection(sitk_img_i.GetDirection())
    new_img.SetOrigin(sitk_img_i.GetOrigin())
    new_img.SetSpacing(sitk_img_i.GetSpacing())
    _, fullflname = os.path.split(img_i)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    i_path = r'./1'
    e_path = r'./2'
    save_path = r'./save'
    i_list = get_listdir(i_path)
    i_list.sort()
    e_list = get_listdir(e_path)
    e_list.sort()

    for i in tqdm.trange(len(i_list)):
        change_label(i_list[i], e_list[i], save_path)