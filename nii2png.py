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


def nii2png(img, save_path):
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    img_arr[img_arr == 1] = 28
    img_arr[img_arr == 2] = 75
    # img_arr[img_arr == 2] = 25
    # img_arr[img_arr == 3] = 149
    # img_arr[img_arr == 4] = 93
    # img_arr[img_arr == 5] = 37
    _, fullflname = os.path.split(img)
    name = fullflname.split('_')[0]
    path = os.path.join(save_path, name)
    os.makedirs(path, exist_ok=True)
    for i in range(img_arr.shape[0]):
        temp = img_arr[i, :, :].astype(np.uint8)
        img_pil = Image.fromarray(temp)
        img_pil.save(os.path.join(path, name + '-1' + str(i).rjust(3, '0') + '.png'))


if __name__ == '__main__':
    img_path = r'Y:\challenge\3\test'
    save_path = r'Y:\challenge\3\test2'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        nii2png(img_list[i], save_path)
