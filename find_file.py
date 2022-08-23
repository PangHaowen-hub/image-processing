import SimpleITK as sitk
import os
from PIL import Image
import numpy as np
from tqdm import trange
import shutil


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def find_path(mask_path, save_path):
    _, fullflname = os.path.split(mask_path)
    shutil.copy(os.path.join(mask_path, 'aorta.nii.gz'), os.path.join(save_path, fullflname))

if __name__ == '__main__':
    img_path = r'H:\CT2CECT\Pulmonary_embolism\segmentation\mask_all'
    save_path = r'H:\CT2CECT\Pulmonary_embolism\segmentation\mask'
    img_list = os.listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        find_path(os.path.join(img_path, img_list[i]), save_path)
