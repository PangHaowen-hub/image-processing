import SimpleITK as sitk
import numpy as np
import os
from tqdm import trange
from scipy.ndimage.filters import convolve


def get_listdir(path):
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


def edge(img_path, save_path):
    sitk_img = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    img_edges = sobel_filters(img_arr)
    new_mask_img = sitk.GetImageFromArray(img_edges)
    new_mask_img.SetDirection(sitk_img.GetDirection())
    new_mask_img.SetSpacing(sitk_img.GetSpacing())
    new_mask_img.SetOrigin(sitk_img.GetOrigin())
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_mask_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    img_path = r'H:\my_lobe_data\after\LL\masks_rename'
    save_path = r'C:\Users\user\Desktop\temp'
    img_list = get_listdir(img_path)
    img_list.sort()

    for i in trange(len(img_list)):
        edge(img_list[i], save_path)
