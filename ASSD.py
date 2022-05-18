import SimpleITK as sitk
import numpy as np
import os
from tqdm import trange
import surface_distance as surfdist
import math


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def ASSD_3d(mask_path, pred_path, lobe_index):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    pred_sitk_img = sitk.ReadImage(pred_path)
    pred_img_arr = sitk.GetArrayFromImage(pred_sitk_img)

    mask_img_arr[mask_img_arr != lobe_index] = 0
    pred_img_arr[pred_img_arr != lobe_index] = 0

    mask_img_arr[mask_img_arr == lobe_index] = 1
    pred_img_arr[pred_img_arr == lobe_index] = 1

    mask_img_arr = mask_img_arr.astype(np.bool_)
    pred_img_arr = pred_img_arr.astype(np.bool_)

    spacing = mask_sitk_img.GetSpacing()
    surface_distances = surfdist.compute_surface_distances(mask_img_arr, pred_img_arr, spacing_mm=spacing)
    asd = surfdist.compute_average_surface_distance(surface_distances)
    return np.mean(asd)


if __name__ == '__main__':
    mask_path = r'F:\my_code\segmentation_3d\data_3d\test\RU\mask'
    pred_path = r'F:\my_code\segmentation_3d\data_3d\test\RU\pred_left_unet3d'
    mask = get_listdir(mask_path)
    mask.sort()
    pred = get_listdir(pred_path)
    pred.sort()
    for lobe_index in range(1, 6):
        asd = 0
        for i in trange(len(mask)):
            asd += ASSD_3d(mask[i], pred[i], lobe_index)
        print(lobe_index, ':', asd / len(mask))

    # asd = 0
    # for i in trange(10):
    #     asd += ASSD_3d(mask[i], pred[i], 2)
    # print(2, ':', asd / len(mask))
