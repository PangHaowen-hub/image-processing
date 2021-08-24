import SimpleITK as sitk
import numpy as np
import os


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def transposeMask(ct_path, mask_path):
    ct_sitk_img = sitk.ReadImage(ct_path)
    ct_img_arr = sitk.GetArrayFromImage(ct_sitk_img)

    print(ct_img_arr.shape)
    print(ct_sitk_img.GetDirection())

    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    mask_img_arr = np.flip(mask_img_arr, axis=1)
    mask_img_arr = np.flip(mask_img_arr, axis=2)

    print(mask_img_arr.shape)
    print(mask_sitk_img.GetDirection())

    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(ct_sitk_img.GetDirection())
    new_mask_img.SetOrigin(ct_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(ct_sitk_img.GetSpacing())
    # sitk.WriteImage(new_mask_img, mask_path[0:-7] + '_transpose.nii.gz')
    sitk.WriteImage(new_mask_img, mask_path)


if __name__ == '__main__':
    img_path = r'C:\Users\Administrator\Desktop\img'
    mask_path = r'C:\Users\Administrator\Desktop\mask'
    ct = get_listdir(img_path)
    mask = get_listdir(mask_path)
    for i in range(len(ct)):
        transposeMask(ct[i], mask[i])