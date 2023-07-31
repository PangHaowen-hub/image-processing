import SimpleITK as sitk
import os
import numpy as np
from tqdm import trange


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.npy':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    nii_path = r'H:\PRM\59_cases_nii\59_cases_nii_i_lung\YANG_GANG_HONG_20181217001040=29_I.nii.gz'
    npy_path = r'C:\Users\user\Desktop\save_npy_path\fakeA\YANG_GANG_HONG_20181217001040=29_I.nii.gz00000_fake_A'
    save_path = r'C:\Users\user\Desktop\save_npy_path\fakeA'
    sitk_img = sitk.ReadImage(nii_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)

    img_list = get_listdir(npy_path)
    img_list.sort()
    new_img = np.zeros_like(img_arr)
    for i in trange(len(img_list)):
        image = np.load(img_list[i])
        new_img[i, :, :] = image
    new_img = sitk.GetImageFromArray(new_img)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetSpacing(sitk_img.GetSpacing())
    new_img.SetOrigin(sitk_img.GetOrigin())
    _, fullflname = os.path.split(nii_path)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))
