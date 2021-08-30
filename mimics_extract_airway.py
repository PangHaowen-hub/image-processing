import SimpleITK as sitk
import numpy as np
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def delete_label(mask_path):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    mask_img_arr[mask_img_arr != 1943] = 0
    mask_img_arr[mask_img_arr == 1943] = 1
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(mask_sitk_img.GetDirection())
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    sitk.WriteImage(new_mask_img, mask_path)


if __name__ == '__main__':
    mask_path = r'D:\github_code\Airway-master\example_data\my_data\temp'
    mask = get_listdir(mask_path)
    for i in range(len(mask)):
        delete_label(mask[i])
