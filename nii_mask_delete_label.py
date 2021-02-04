import SimpleITK as sitk
import numpy as np
import os


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def delete_label(mask_path):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    mask_img_arr[(mask_img_arr == 4) | (mask_img_arr == 5)] = 0
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    sitk.WriteImage(new_mask_img, mask_path)


if __name__ == '__main__':
    mask_path = r'F:\my_lobe_data\after\RL\delete_left_labe_mask'
    mask = get_listdir(mask_path)
    for i in range(len(mask)):
        delete_label(mask[i])
