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
    # CT_path = r'F:\my_code\pelvic-to-brain\nnUNet-CT-MRI\nnUNet_raw\Dataset111_brain\imagesTr\1BA001_0000.nii.gz'
    # MRI_path = r'F:\my_code\pelvic-to-brain\nnUNet-CT-MRI\nnUNet_raw\Dataset111_brain\labelsTr\1BA001.nii.gz'

    CT_path = r'ct.nii.gz'
    MRI_path = r'cbct.nii.gz'
    save_path = r'Difference_cbct.npy'

    sitk_CT = sitk.ReadImage(CT_path)
    CT_arr = sitk.GetArrayFromImage(sitk_CT)

    sitk_MRI = sitk.ReadImage(MRI_path)
    MRI_arr = sitk.GetArrayFromImage(sitk_MRI)

    f_CT = np.fft.fft2(CT_arr[80, :, :])
    fshift_CT = np.fft.fftshift(f_CT)
    fimg_CT = np.log(np.abs(fshift_CT))

    f_MRI = np.fft.fft2(MRI_arr[80, :, :])
    fshift_MRI = np.fft.fftshift(f_MRI)
    fimg_MRI = np.log(np.abs(fshift_MRI))

    Difference = np.abs(fimg_CT - fimg_MRI)
    np.save(save_path, Difference)
    np.save('ct.npy', fimg_CT)
    np.save('cbct.npy', fimg_MRI)



