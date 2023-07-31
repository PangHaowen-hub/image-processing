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
        fimg_CT_fre = np.abs(fshift_CT)  # CT频谱
        fimg_CT_fre[fimg_CT_fre != 1000] = 1000
        fimg_CT_pha = np.angle(fshift_CT)  # CT相位

        f_MRI = np.fft.fftn(MRI_arr)
        fshift_MRI = np.fft.fftshift(f_MRI)
        fimg_MRI_fre = np.abs(fshift_MRI)  # MRI频谱
        fimg_MRI_fre[fimg_MRI_fre != 1000] = 1000
        fimg_MRI_pha = np.angle(fshift_MRI)  # MRI相位

        fimg_rec_CT = np.zeros(CT_arr.shape, dtype=complex)
        fimg_rec_CT.real = fimg_CT_fre * np.cos(fimg_CT_pha)
        fimg_rec_CT.imag = fimg_CT_fre * np.sin(fimg_CT_pha)
        ifshift_CT = np.fft.ifftshift(fimg_rec_CT)
        rec_CT = np.real(np.fft.ifftn(ifshift_CT))
        new_temp = sitk.GetImageFromArray(rec_CT)
        new_temp.CopyInformation(sitk_CT)
        sitk.WriteImage(new_temp, os.path.join(save_path, 'CT_Rec.nii.gz'))

        fimg_rec_MRI = np.zeros(MRI_arr.shape, dtype=complex)
        fimg_rec_MRI.real = fimg_MRI_fre * np.cos(fimg_MRI_pha)
        fimg_rec_MRI.imag = fimg_MRI_fre * np.sin(fimg_MRI_pha)
        ifshift_MRI = np.fft.ifftshift(fimg_rec_MRI)
        rec_MRI = np.real(np.fft.ifftn(ifshift_MRI))
        new_temp = sitk.GetImageFromArray(rec_MRI)
        new_temp.CopyInformation(sitk_MRI)
        sitk.WriteImage(new_temp, os.path.join(save_path, 'MRI_Rec.nii.gz'))


