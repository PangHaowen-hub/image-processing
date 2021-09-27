import SimpleITK as sitk
from tqdm import trange
import os
import numpy as np


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(l_mask):
    l_mask_sitk_img = sitk.ReadImage(l_mask)
    l_mask_img_arr = sitk.GetArrayFromImage(l_mask_sitk_img)
    t = np.unique(l_mask_img_arr)
    print(t)


if __name__ == '__main__':
    l_mask_path = r'G:\my_lobe_data\after\RL\masks_rename_change_label'
    r_mask = get_listdir(l_mask_path)
    r_mask.sort()
    for i in trange(len(r_mask)):
        add_label(r_mask[i])
