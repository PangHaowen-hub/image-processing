import SimpleITK as sitk
import os

import numpy as np


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    l_mask_path = r'F:\segment_registration\Registration\original_image\RL_lobe'
    l_mask = get_listdir(l_mask_path)
    l_mask.sort()
    l = []
    for i in l_mask:
        sitk_img = sitk.ReadImage(i)
        img_arr = sitk.GetArrayFromImage(sitk_img)
        l.append(img_arr.shape)
    shape = np.asarray(l)
    print(np.max(shape, 0))
