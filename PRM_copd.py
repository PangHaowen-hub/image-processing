import SimpleITK as sitk
import numpy as np
from tqdm import trange
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(i, e, savepath):
    sitk_i = sitk.ReadImage(i)
    i_arr = sitk.GetArrayFromImage(sitk_i)
    sitk_e = sitk.ReadImage(e)
    e_arr = sitk.GetArrayFromImage(sitk_e)
    save_arr = np.zeros_like(i_arr)
    save_arr[i_arr > -950] += 1
    save_arr[e_arr > -856] += 1
    save_arr += 1
    save_arr[i_arr == -1000] = 0

    new_img = sitk.GetImageFromArray(save_arr)
    new_img.SetDirection(sitk_i.GetDirection())
    new_img.SetOrigin(sitk_i.GetOrigin())
    new_img.SetSpacing(sitk_i.GetSpacing())
    _, fullflname = os.path.split(i)
    sitk.WriteImage(new_img, os.path.join(savepath, fullflname))


if __name__ == '__main__':
    i_path = r'E:\registration_e2i\instances\i_lung'
    e_path = r'E:\registration_e2i\instances\e2i'
    save_path = r'E:\registration_e2i\instances\res'

    i_list = get_listdir(i_path)
    i_list.sort()
    e_list = get_listdir(e_path)
    e_list.sort()

    for i in trange(len(i_list)):
        add_label(i_list[i], e_list[i], save_path)
