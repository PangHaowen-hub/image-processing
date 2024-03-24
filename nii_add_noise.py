import numpy as np
import os
import SimpleITK as sitk
import tqdm


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def normalization(img_path, save_path):
    sitk_img = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    noise = np.random.normal(0, 10, img_arr.shape)
    img_arr = img_arr + noise
    new_img = sitk.GetImageFromArray(img_arr)
    new_img.CopyInformation(sitk_img)
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    img_path = r'C:\Users\40702\Desktop\temp_resample'
    save_path = r'C:\Users\40702\Desktop\temp_resample_add_noise'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in tqdm.tqdm(img_list):
        normalization(i, save_path)
