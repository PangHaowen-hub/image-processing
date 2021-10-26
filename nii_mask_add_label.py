import SimpleITK as sitk
from tqdm import trange
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(l_mask, r_mask, add_mask_path):
    l_mask_sitk_img = sitk.ReadImage(l_mask)
    l_mask_img_arr = sitk.GetArrayFromImage(l_mask_sitk_img)
    r_mask_sitk_img = sitk.ReadImage(r_mask)
    r_mask_img_arr = sitk.GetArrayFromImage(r_mask_sitk_img)
    r_mask_img_arr[l_mask_img_arr == 4] = 4
    r_mask_img_arr[l_mask_img_arr == 5] = 5
    new_mask_img = sitk.GetImageFromArray(r_mask_img_arr)
    new_mask_img.SetDirection(r_mask_sitk_img.GetDirection())
    new_mask_img.SetOrigin(r_mask_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(r_mask_sitk_img.GetSpacing())
    _, fullflname = os.path.split(l_mask)
    sitk.WriteImage(new_mask_img, os.path.join(add_mask_path, fullflname))


if __name__ == '__main__':
    l_mask_path = r'F:\my_code\segmentation_3d\data_SJ\after\pred_3d\RL\VNet\left'
    r_mask_path = r'F:\my_code\segmentation_3d\data_SJ\after\pred_3d\RL\VNet\right'
    add_mask_path = r'F:\my_code\segmentation_3d\data_SJ\after\pred_3d\RL\VNet'
    l_mask = get_listdir(l_mask_path)
    l_mask.sort()
    r_mask = get_listdir(r_mask_path)
    r_mask.sort()
    for i in trange(len(l_mask)):
        add_label(l_mask[i], r_mask[i], add_mask_path)
