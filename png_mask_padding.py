import cv2
import os
from PIL import Image
import numpy as np


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


def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


color_map = get_color_map_list(256)
path = r'E:\CAS\github_code\AttaNet_1280_720\data\satellite_gray\val_masks'
img_list = get_listdir(path, '.png')
desired_size = 1280
for i in img_list:
    _, fullflname = os.path.split(i)

    im = Image.open(i)
    im = np.array(im)
    old_size = im.shape[:2]  # old_size is in (height, width) format

    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])

    # new_size should be in (width, height) format

    im = cv2.resize(im, (new_size[1], new_size[0]), interpolation=cv2.INTER_NEAREST)

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)
    lbl_pil = Image.fromarray(new_im.astype(np.uint8), mode='P')
    lbl_pil.putpalette(color_map)
    lbl_pil.save(os.path.join('E:/CAS/github_code/AttaNet_1280_720/data/satellite_gray/satellite_1280/val_mask_1280',
                              fullflname)[:-4] + '.png')
