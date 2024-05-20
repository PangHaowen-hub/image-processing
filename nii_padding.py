import torchio as tio
import numpy as np
import os
import SimpleITK as sitk
import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def pad(img_path, save_path):
    sitk_img = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)

    img_arr = np.expand_dims(img_arr, axis=0)
    pad_transform = tio.transforms.CropOrPad((96, 96, 96), padding_mode=0)  # TODO:修改Padding值
    new_arr = pad_transform(img_arr)
    new_arr = np.squeeze(new_arr, 0)
    new_img = sitk.GetImageFromArray(new_arr)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetOrigin(sitk_img.GetOrigin())
    new_img.SetSpacing(sitk_img.GetSpacing())
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    img_path = r'G:\stroke2022\MICCAI_Stroke_2022\MASK'
    save_path = r'G:\stroke2022\MICCAI_Stroke_2022\MASK_padding'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in tqdm.tqdm(img_list):
        pad(i, save_path)
