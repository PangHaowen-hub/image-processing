"""
使用术前模型分割后mask中左肺label置为4或5
"""

import SimpleITK as sitk
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(mask, final_mask_path):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    # LL:4  LU:5
    # mask_img_arr[(mask_img_arr == 4) | (mask_img_arr == 5)] = 5
    mask_img_arr[mask_img_arr == 2] = 3
    mask_img_arr[mask_img_arr == 1] = 2
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, final_mask_path + fullflname)


if __name__ == '__main__':
    mask_path = r'F:\my_lobe_data\after\RU\_right_predict'
    final_mask_path = 'F:/my_lobe_data/after/RU/_right_predict/'

    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        add_label(mask[i], final_mask_path)
