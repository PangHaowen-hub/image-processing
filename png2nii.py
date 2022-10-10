import SimpleITK as sitk
import os
from PIL import Image
import numpy as np
from tqdm import trange


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_listdir_2(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if file.split('_')[-1] == 'fake.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    nii_path = r'E:\PRM\10-10\YANG_GANG_HONG_20181217001040=29_I.nii.gz'
    png_path = r'E:\PRM\10-10\cycleswinunetr\case1'
    save_path = r'E:\PRM\10-10\YANG_GANG_HONG_20181217001040=29_E_cycleswinunetr.nii.gz'
    sitk_img = sitk.ReadImage(nii_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)

    img_list = get_listdir_2(png_path)
    img_list.sort()
    new_mask = np.zeros_like(img_arr)
    for i in trange(len(img_list)):
        image = Image.open(img_list[i])
        new_mask[i, :, :] = np.asarray(image)[:,:,0] / 255 * 1000 - 1000
    new_mask = sitk.GetImageFromArray(new_mask)
    new_mask.SetDirection(sitk_img.GetDirection())
    new_mask.SetSpacing(sitk_img.GetSpacing())
    new_mask.SetOrigin(sitk_img.GetOrigin())
    sitk.WriteImage(new_mask, save_path)
