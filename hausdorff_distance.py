import SimpleITK as sitk
import numpy as np
import os
from tqdm import trange
from hausdorff import hausdorff_distance
from scipy.ndimage import convolve
import copy


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def sobel_filters(img):
    Kx = np.array([[[1, 0, -1], [2, 0, -2], [1, 0, -1]], [[2, 0, -2], [4, 0, -4], [2, 0, -2]],
                   [[1, 0, -1], [2, 0, -2], [1, 0, -1]]], np.float32)
    Ky = np.array([[[1, 2, 1], [0, 0, 0], [-1, -2, -1]], [[2, 4, 2], [0, 0, 0], [-2, -4, -2]],
                   [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]], np.float32)
    Kz = np.array([[[1, 2, 1], [2, 4, 2], [1, 2, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[-1, -2, -1], [-2, -4, -2], [-1, -2, -1]]], np.float32)

    Ix = convolve(img, Kx)
    Iy = convolve(img, Ky)
    Iz = convolve(img, Kz)

    G = np.sqrt(Ix ** 2 + Iy ** 2 + Iz ** 2)
    G = G / G.max()
    return G


def HD_3d(mask_path, pred_path):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    pred_sitk_img = sitk.ReadImage(pred_path)
    pred_img_arr = sitk.GetArrayFromImage(pred_sitk_img)
    # pred_img_arr = pred_img_arr.astype(np.uint16)
    mask_1 = np.ones_like(mask_img_arr)
    mask_1[mask_img_arr != 1] = 0
    mask_2 = np.ones_like(mask_img_arr)
    mask_2[mask_img_arr != 2] = 0
    mask_3 = np.ones_like(mask_img_arr)
    mask_3[mask_img_arr != 3] = 0
    mask_4 = np.ones_like(mask_img_arr)
    mask_4[mask_img_arr != 4] = 0
    mask_5 = np.ones_like(mask_img_arr)
    mask_5[mask_img_arr != 5] = 0

    pred_1 = np.ones_like(pred_img_arr)
    pred_1[pred_img_arr != 1] = 0
    pred_2 = np.ones_like(pred_img_arr)
    pred_2[pred_img_arr != 2] = 0
    pred_3 = np.ones_like(pred_img_arr)
    pred_3[pred_img_arr != 3] = 0
    pred_4 = np.ones_like(pred_img_arr)
    pred_4[pred_img_arr != 4] = 0
    pred_5 = np.ones_like(pred_img_arr)
    pred_5[pred_img_arr != 5] = 0

    mask_edge_1 = sobel_filters(mask_1)
    mask_edge_2 = sobel_filters(mask_2)
    mask_edge_3 = sobel_filters(mask_3)
    mask_edge_4 = sobel_filters(mask_4)
    mask_edge_5 = sobel_filters(mask_5)

    pred_edge_1 = sobel_filters(pred_1)
    pred_edge_2 = sobel_filters(pred_2)
    pred_edge_3 = sobel_filters(pred_3)
    pred_edge_4 = sobel_filters(pred_4)
    pred_edge_5 = sobel_filters(pred_5)

    mask_index1 = np.argwhere(mask_edge_1 != 0)
    mask_index2 = np.argwhere(mask_edge_2 != 0)
    mask_index3 = np.argwhere(mask_edge_3 != 0)
    mask_index4 = np.argwhere(mask_edge_4 != 0)
    mask_index5 = np.argwhere(mask_edge_5 != 0)

    pred_index1 = np.argwhere(pred_edge_1 != 0)
    pred_index2 = np.argwhere(pred_edge_2 != 0)
    pred_index3 = np.argwhere(pred_edge_3 != 0)
    pred_index4 = np.argwhere(pred_edge_4 != 0)
    pred_index5 = np.argwhere(pred_edge_5 != 0)

    hd1 = hausdorff_distance(mask_index1, pred_index1, distance='euclidean') * 0.7
    hd2 = hausdorff_distance(mask_index2, pred_index2, distance='euclidean') * 0.7
    hd3 = hausdorff_distance(mask_index3, pred_index3, distance='euclidean') * 0.7
    hd4 = hausdorff_distance(mask_index4, pred_index4, distance='euclidean') * 0.7
    hd5 = hausdorff_distance(mask_index5, pred_index5, distance='euclidean') * 0.7

    return hd1, hd2, hd3, hd4, hd5


if __name__ == '__main__':
    mask_path = r'H:\my_lobe_data\before\all_lobe_512\test_mask\ground_truth'
    pred_path = r'H:\my_lobe_data\before\all_lobe_512\test_mask\test_mask_best'
    mask = get_listdir(mask_path)
    mask.sort()
    pred = get_listdir(pred_path)
    pred.sort()
    HD1, HD2, HD3, HD4, HD5 = 0, 0, 0, 0, 0
    for i in trange(len(mask)):
        hd1, hd2, hd3, hd4, hd5 = HD_3d(mask[i], pred[i])
        HD1 += hd1
        HD2 += hd2
        HD3 += hd3
        HD4 += hd4
        HD5 += hd5

    print(HD1 / len(mask))
    print(HD2 / len(mask))
    print(HD3 / len(mask))
    print(HD4 / len(mask))
    print(HD5 / len(mask))
