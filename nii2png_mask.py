import SimpleITK as sitk
import os
from PIL import Image
import numpy as np
from tqdm import trange


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_color_map_list(num_classes):
    num_classes += 1
    color_map = num_classes * [0, 0, 0]
    for i in range(0, num_classes):
        j = 0
        lab = i
        while lab:
            color_map[i * 3] |= (((lab >> 0) & 1) << (7 - j))
            color_map[i * 3 + 1] |= (((lab >> 1) & 1) << (7 - j))
            color_map[i * 3 + 2] |= (((lab >> 2) & 1) << (7 - j))
            j += 1
            lab >>= 3
    color_map = color_map[3:]
    return color_map


def nii2png(img, mask, save_path_img, save_path_mask):
    color_map = get_color_map_list(256)
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    MIN_BOUND = -1000.0
    MAX_BOUND = 400.0
    img_arr[img_arr > MAX_BOUND] = MAX_BOUND
    img_arr[img_arr < MIN_BOUND] = MIN_BOUND
    img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND) * 255
    sitk_mask = sitk.ReadImage(mask)
    mask_arr = sitk.GetArrayFromImage(sitk_mask)
    if img_arr.shape != mask_arr.shape:
        print('图像和mask大小不同')
    _, fullflname = os.path.split(img)
    for i in trange(img_arr.shape[0]):
        temp = img_arr[i, :, :].astype(np.uint8)
        img_pil = Image.fromarray(temp)
        img_pil.save(os.path.join(save_path_img, fullflname + '_' + str(i) + '.png'))
        mask_pil = Image.fromarray(mask_arr[i, :, :].astype(np.uint8), mode='P')
        mask_pil.putpalette(color_map)
        mask_pil.save(os.path.join(save_path_mask, fullflname + '_' + str(i) + '.png'))


if __name__ == '__main__':
    img_path = r'F:\my_lobe_data\after\RM\imgs_rename'
    mask_path = r'F:\my_lobe_data\after\RM\masks_rename'
    save_path_img = r'D:\my_code\segmentation_3d\data\images\train\after\RML'
    save_path_mask = r'D:\my_code\segmentation_3d\data\masks\train\after\RML'

    img_list = get_listdir(img_path)
    img_list.sort()
    mask_list = get_listdir(mask_path)
    mask_list.sort()
    for i in trange(len(img_list)):
        nii2png(img_list[i], mask_list[i], save_path_img, save_path_mask)
