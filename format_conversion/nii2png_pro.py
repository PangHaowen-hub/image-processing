import SimpleITK as sitk
import os
from PIL import Image
import numpy as np
from tqdm import trange
import nibabel as nib


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def nii2png(img, save_path):  # 每个nii一个文件夹
    img_nib = nib.load(img)
    affine = img_nib.affine
    orientation = nib.aff2axcodes(affine)

    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    # 预期方向L, P, S, 方向如果不是L, P, S的话就反转矩阵
    if orientation[0] == 'R':
        img_arr = img_arr[::-1,:,:]
    if orientation[1] == 'A':
        img_arr = img_arr[:,::-1,:]
    if orientation[2] == 'I':
        img_arr = img_arr[:,:,::-1]
    MIN_BOUND = 0.0
    MAX_BOUND = 1000.0
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


if __name__ == '__main__':
    img_path = r'C:\Users\40702\Desktop'
    save_path = r'C:\Users\40702\Desktop'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        nii2png(img_list[i], save_path)
