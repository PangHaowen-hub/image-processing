import SimpleITK as sitk
import numpy as np
import os
import tqdm


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def resample(img_path, save_path):
    mask_sitk_img = sitk.ReadImage(img_path)
    img_shape = mask_sitk_img.GetSize()
    img_spacing = mask_sitk_img.GetSpacing()
    # 设置一个Filter
    resample = sitk.ResampleImageFilter()
    # 设置插值方式
    resample.SetInterpolator(sitk.sitkLinear)
    # 默认像素值
    resample.SetDefaultPixelValue(-1000)
    newspacing = [0.8, 0.8, 0.8]
    resample.SetOutputSpacing(newspacing)
    resample.SetOutputOrigin(mask_sitk_img.GetOrigin())
    resample.SetOutputDirection(mask_sitk_img.GetDirection())
    new_size = np.asarray(img_shape) * np.asarray(img_spacing) / np.asarray(newspacing)
    new_size = new_size.astype(int).tolist()
    resample.SetSize(new_size)
    new = resample.Execute(mask_sitk_img)
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    img_path = r'H:\CT2CECT\registration\data\cect_a_lung'
    save_path = r'H:\CT2CECT\registration\data\cect_a_lung_resample'
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in tqdm.tqdm(img_list):
        resample(i, save_path)
