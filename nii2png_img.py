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


def nii2png(img, save_path):  # 每个nii一个文件夹
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    MIN_BOUND = -1000.0
    MAX_BOUND = 0.0
    img_arr[img_arr > MAX_BOUND] = MAX_BOUND
    img_arr[img_arr < MIN_BOUND] = MIN_BOUND
    img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND) * 255
    _, fullflname = os.path.split(img)
    path = os.path.join(save_path, fullflname[:-7])
    os.mkdir(path)
    for i in trange(img_arr.shape[0]):
        temp = img_arr[i, :, :].astype(np.uint8)
        img_pil = Image.fromarray(temp)
        img_pil.save(os.path.join(path, str(i).rjust(3, '0') + '.png'))


def nii2png_path(img, save_path):  # 所有图像同一个文件夹
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    MIN_BOUND = -1000.0
    MAX_BOUND = 0.0
    img_arr[img_arr > MAX_BOUND] = MAX_BOUND
    img_arr[img_arr < MIN_BOUND] = MIN_BOUND
    img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND) * 255
    _, fullflname = os.path.split(img)
    for i in trange(img_arr.shape[0]):
        temp = img_arr[i, :, :].astype(np.uint8)
        img_pil = Image.fromarray(temp)
        img_pil.save(os.path.join(save_path, fullflname + str(i).rjust(5, '0') + '.png'))


if __name__ == '__main__':
    img_path = r'H:\PRM\59_cases_nii\registration_e2i\output_1'
    save_path = r'F:\github_code\pytorch-CycleGAN-and-pix2pix-master\datasets\PRM\e'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        # nii2png(img_list[i], save_path)
        nii2png_path(img_list[i], save_path)

