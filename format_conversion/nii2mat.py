import scipy.io
import numpy as np
import SimpleITK as sitk
import os
import tqdm


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def img_rectity(img, path):
    img_sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(img_sitk_img)
    MIN_BOUND = -1000.0
    MAX_BOUND = 0.0
    img_arr[img_arr > MAX_BOUND] = MAX_BOUND
    img_arr[img_arr < MIN_BOUND] = MIN_BOUND
    img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    scipy.io.savemat(os.path.join(path, 'data_train_contrast1.mat'), {'data': img_arr})


if __name__ == '__main__':
    img_path = r'H:\PRM\59_cases_nii\59_cases_nii_i_lung'  # img路径
    save_path = r'F:\github_code\SynDiff-main\data'  # 保存路径
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in tqdm.trange(len(img_list)):
        img_rectity(img_list[i], save_path)
