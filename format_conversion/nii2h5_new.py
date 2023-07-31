import os
import h5py
import numpy as np
import SimpleITK as sitk
from tqdm import trange


def nii2h5(img_name, label_name, save_path):
    """
    Converts a nifti file to riesling format .h5 image file
    """
    img = sitk.ReadImage(img_name)
    img_data = sitk.GetArrayFromImage(img)

    label = sitk.ReadImage(label_name)
    label_data = sitk.GetArrayFromImage(label)

    _, fullflname = os.path.split(img_name)
    output_name = os.path.join(save_path, fullflname[:-7] + '.h5')

    h5 = h5py.File(output_name, 'w')
    h5.create_dataset('raw', data=img_data)
    h5.create_dataset('label', data=label_data)
    h5.close()


def get_nii_list(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_h5_list(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.h5':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'H:\PRM\59_cases_nii\segmentation\59_cases_nii_i_lung'
    label_path = r'H:\PRM\59_cases_nii\segmentation\PRM_rename_I'

    save_path = r'F:\github_code\pytorch-3dunet-master\data'
    img_list = get_nii_list(img_path)
    img_list.sort()

    label_list = get_nii_list(label_path)
    label_list.sort()
    for i in trange(len(img_list)):
        nii2h5(img_list[i], label_list[i], save_path)
