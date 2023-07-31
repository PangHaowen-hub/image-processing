import SimpleITK as sitk
import os
import numpy as np
from tqdm import trange


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    CT_path = r'F:\my_code\pelvic-to-brain\nnUNet-CT-MRI\nnUNet_raw\Dataset111_brain\imagesTr'
    MRI_path = r'F:\my_code\pelvic-to-brain\nnUNet-CT-MRI\nnUNet_raw\Dataset111_brain\labelsTr'

    save_path = r'./'
    ct_list = get_listdir(CT_path)
    ct_list.sort()

    mri_list = get_listdir(MRI_path)
    mri_list.sort()
    for i in trange(len(ct_list)):
        sitk_CT = sitk.ReadImage(ct_list[i])
        CT_arr = sitk.GetArrayFromImage(sitk_CT)

        sitk_MRI = sitk.ReadImage(mri_list[i])
        MRI_arr = sitk.GetArrayFromImage(sitk_MRI)

        f_CT = np.fft.fftn(CT_arr)
        fshift_CT = np.fft.fftshift(f_CT)

        f_MRI = np.fft.fftn(MRI_arr)
        fshift_MRI = np.fft.fftshift(f_MRI)

        # 设置高通滤波器
        # fshift_CT[:100, :100, :100] = 0
        # fshift_CT[-100:, -100:, -100:] = 0
        #
        # fshift_MRI[:100, :100, :100] = 0
        # fshift_MRI[-100:, -100:, -100:] = 0

        # 设置低通滤波器
        # x, y, z = int(CT_arr.shape[0] / 2), int(CT_arr.shape[1] / 2), int(CT_arr.shape[2] / 2)
        # num = 2
        # fshift_CT[x-num:x+num, y-num:y+num, z-num:z+num] = 0
        # fshift_MRI[x-num:x+num, y-num:y+num, z-num:z+num] = 0

        ifshift_CT = np.fft.ifftshift(fshift_CT)
        ifshift_MRI = np.fft.ifftshift(fshift_MRI)

        rec_CT = np.real(np.fft.ifftn(ifshift_CT))
        rec_MRI = np.real(np.fft.ifftn(ifshift_MRI))

        new_CT = sitk.GetImageFromArray(rec_CT)
        new_CT.CopyInformation(sitk_CT)
        _, fullflname = os.path.split(ct_list[i])
        sitk.WriteImage(new_CT, os.path.join(save_path, fullflname))

        new_MRI = sitk.GetImageFromArray(rec_MRI)
        new_MRI.CopyInformation(sitk_MRI)
        _, fullflname = os.path.split(mri_list[i])
        sitk.WriteImage(new_MRI, os.path.join(save_path, fullflname))
