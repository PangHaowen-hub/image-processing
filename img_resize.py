import cv2
import os

import tqdm


def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


path = r'F:\my_code\zhanghe\pytorch-CycleGAN-and-pix2pix-master\results\he-GAN\100'
save_path = r'F:\my_code\zhanghe\pytorch-CycleGAN-and-pix2pix-master\results\he-GAN\100'

img_list = get_listdir(path, '.png')
img_list.sort()

for i in tqdm.tqdm(img_list):
    _, fullflname = os.path.split(i)
    im = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    im = cv2.resize(im, (64, 64))
    cv2.imwrite(os.path.join(save_path, fullflname), im)
