import numpy as np
import SimpleITK as sitk
from tqdm import trange
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def createMIP(np_img, slices_num=15):  # TODO:可修改此处调整投影的切片数
    # slice_num is the number of slices for maximum intensity projection
    img_shape = np_img.shape
    np_mip = np.zeros(img_shape)
    for i in range(img_shape[0]):
        start = max(0, i - slices_num)
        np_mip[i, :, :] = np.amax(np_img[start:i + 1], 0)
    return np_mip


def mip(img_path, save_path):
    sitk_img = sitk.ReadImage(img_path)
    np_img = sitk.GetArrayFromImage(sitk_img)
    np_mip = createMIP(np_img)
    sitk_mip = sitk.GetImageFromArray(np_mip)
    sitk_mip.SetOrigin(sitk_img.GetOrigin())
    sitk_mip.SetSpacing(sitk_img.GetSpacing())
    sitk_mip.SetDirection(sitk_img.GetDirection())
    writer = sitk.ImageFileWriter()
    _, fullflname = os.path.split(img_path)
    writer.SetFileName(os.path.join(save_path, fullflname))
    writer.Execute(sitk_mip)


if __name__ == '__main__':
    img_path = r'I:\paper\8-vessel_map\COPD\yxy\img'
    save_path = r'I:\paper\8-vessel_map\COPD\yxy\MIP_3d'
    img_list = get_listdir(img_path)
    img_list.sort()

    for i in trange(len(img_list)):
        mip(img_list[i], save_path)
