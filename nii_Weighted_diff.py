import SimpleITK as sitk
import os
from tqdm import trange


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def difference(img1_path, img2_path, save_path, weight):
    img1 = sitk.ReadImage(img1_path)
    img1_arr = sitk.GetArrayFromImage(img1)
    img2 = sitk.ReadImage(img2_path)
    img2_arr = sitk.GetArrayFromImage(img2)
    diff_img_arr = img1_arr - weight * img2_arr
    diff_img = sitk.GetImageFromArray(diff_img_arr)
    diff_img.CopyInformation(img1)

    sitk.WriteImage(diff_img, os.path.join(save_path, str(weight) + '.nii.gz'))


if __name__ == '__main__':
    img1_path = r'C:\Users\40702\Desktop\T1_25_dose.nii.gz'
    img2_path = r'C:\Users\40702\Desktop\T1_0_dose.nii.gz'
    save_path = r'C:\Users\40702\Desktop\weighted_diff'
    difference(img1_path, img2_path, save_path, 0.65)
