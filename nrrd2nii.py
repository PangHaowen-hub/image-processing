import SimpleITK as sitk
from tqdm import trange
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.nrrd':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(img, save_path):
    sitk_img = sitk.ReadImage(img)
    _, fullflname = os.path.split(img)
    sitk.WriteImage(sitk_img, os.path.join(save_path, fullflname[:-5] + '.nii.gz'))


if __name__ == '__main__':
    img_path = r'F:\data\Train_Masks'
    save_path = r'F:\data\Train_Masks_nii'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        add_label(img_list[i], save_path)
