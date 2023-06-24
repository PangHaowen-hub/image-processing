import SimpleITK as sitk
import numpy as np
import cv2
import os
import copy
import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def calculate_map(img_path, save_path):
    _, fullflname = os.path.split(img_path)
    img_sitk_img = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(img_sitk_img)

    img_arr[img_arr < -1000] = -1000
    img_arr[img_arr > 1000] = 1000

    shape = img_arr.shape[0]

    new_img_arr_1 = img_arr[:int(shape / 3), :, :]
    new_img_arr_2 = img_arr[int(shape / 3):int(shape * 2 / 3), :, :]
    new_img_arr_3 = img_arr[int(shape * 2 / 3):int(shape), :, :]

    max_pro_1 = np.max(new_img_arr_1, axis=0)
    max_pro_2 = np.max(new_img_arr_2, axis=0)
    max_pro_3 = np.max(new_img_arr_3, axis=0),

    np.save(os.path.join(save_path, fullflname + '_1.npy'), max_pro_1)
    np.save(os.path.join(save_path, fullflname + '_2.npy'), max_pro_2)
    np.save(os.path.join(save_path, fullflname + '_3.npy'), max_pro_3)


if __name__ == '__main__':
    img_path_source = r'I:\paper\8-vessel_map\COPD\yxy\img'
    save_map_path = r'I:\paper\8-vessel_map\COPD\yxy\MIP_2d'
    img_list = get_listdir(img_path_source)
    img_list.sort()
    for i in tqdm.trange(len(img_list)):
        calculate_map(img_list[i], save_map_path)
