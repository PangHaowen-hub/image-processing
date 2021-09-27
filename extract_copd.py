import SimpleITK as sitk
import os
import numpy as np
from PIL import Image


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


def copd(img, mask, save_path):
    color_map = get_color_map_list(256)  # 设置color_map 方便查看
    img_sitk = sitk.ReadImage(img)
    mask_sitk = sitk.ReadImage(mask)
    img_arr = sitk.GetArrayFromImage(img_sitk)
    mask_arr = sitk.GetArrayFromImage(mask_sitk)
    index = np.unique(np.where(mask_arr != 0)[0])  # 找被标注的层

    # normalization
    MIN_BOUND = -1000.0
    MAX_BOUND = 400.0
    img_arr[img_arr > MAX_BOUND] = MAX_BOUND
    img_arr[img_arr < MIN_BOUND] = MIN_BOUND
    img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND) * 255
    # new_img_arry = img_arr[index, :, :]
    # new_mask_arry = mask_arr[index, :, :]

    for i in index:
        new_img = img_arr[i, :, :]
        new_mask = mask_arr[i, :, :]
        img_pil = Image.fromarray(new_img.astype(np.uint8))
        img_pil.save(os.path.join(save_path, 'img' + str(i + 1) + '.png'))
        # mask_pil = Image.fromarray(new_mask)
        mask_pil = Image.fromarray(new_mask.astype(np.uint8), mode='P')
        mask_pil.putpalette(color_map)
        mask_pil.save(os.path.join(save_path, 'mask' + str(i + 1) + '.png'))


if __name__ == '__main__':
    img_path = r'H:\data\img.nii.gz'
    mask_path = r'H:\data\1.nii.gz'
    save_path = r'H:\data'
    copd(img_path, mask_path, save_path)
