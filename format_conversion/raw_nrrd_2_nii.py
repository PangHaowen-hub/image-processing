import SimpleITK as sitk
import os
from glob import glob
import nrrd
import nibabel as nib
import numpy as np


def get_listdir(path):  # 获取目录下所有nrrd格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.nrrd':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list

def get_listdir_mhd(path):  # 获取目录下所有nrrd格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.mhd':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def raw2nii(mhd_path, nii_path):
    mhd = sitk.ReadImage(mhd_path)
    temp = nii_path + '\\' + mhd_path.split('\\')[-1][:-3] + 'nii.gz'
    # temp = mhd_path.split('\\')[-1][:-3] + 'nii.gz'
    sitk.WriteImage(mhd, temp)


if __name__ == '__main__':
    # nrrd_path = r'F:\references_1_data\automatic_pulmonary_lobe_segmentation_using_deep_learning-master\annotations'
    # nrrd_path_list = get_listdir(nrrd_path)
    # nii_path = r'F:\references_1_data\automatic_pulmonary_lobe_segmentation_using_deep_learning-master\annotations_nii'
    # for file in nrrd_path_list:
    #     # load nrrd
    #     _nrrd = nrrd.read(file)
    #     data = _nrrd[0]
    #     data[data > 8] = 0
    #     data[data == 4] = 1
    #     data[data == 5] = 2
    #     data[data == 6] = 3
    #     data[data == 7] = 4
    #     data[data == 8] = 5
    #     data = np.transpose(data, (2, 1, 0))
    #     header = _nrrd[1]
    #     new_mask_img1 = sitk.GetImageFromArray(data)
    #     # direction = (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, -1.0)
    #     # new_mask_img1.SetDirection(direction)
    #     # new_mask_img1.SetOrigin(header['space origin'])
    #     Spacing = list(np.max(header['space directions'], 0))
    #     new_mask_img1.SetSpacing(Spacing)
    #     temp_path = os.path.join(nii_path, file.split('\\')[-1].split('_')[0] + '.nii.gz')
    #     sitk.WriteImage(new_mask_img1, temp_path)

    mhd_path = r'F:\LOLA11\lola11'
    nii_path = r'F:\LOLA11\lola11_nii'
    mhd_path_list = get_listdir_mhd(mhd_path)
    for i in mhd_path_list:
        raw2nii(i, nii_path)
