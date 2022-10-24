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


def nii2dcm(img, save_path):  # 所有图像同一个文件夹
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    img_arr[img_arr > 0] = 0
    img_arr[img_arr < -1000] = -1000
    new_img = sitk.GetImageFromArray(img_arr)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetOrigin(sitk_img.GetOrigin())
    new_img.SetSpacing(sitk_img.GetSpacing())
    _, fullflname = os.path.split(img)
    for i in range(img_arr.shape[0]):
        new_image = new_img[:, :, i]
        sitk.WriteImage(new_image, os.path.join(save_path, fullflname + str(i).rjust(5, '0') + '.dcm'))


if __name__ == '__main__':
    img_path = r'H:\PRM\59_cases_nii\registration_e2i\output_1'
    save_path = r'F:\my_code\copd_PRM\CycleResViT-PRM\datasets\PRM_dcm\trainB'
    img_list = get_listdir(img_path)
    img_list.sort()
    img_list = img_list
    for i in trange(len(img_list)):
        nii2dcm(img_list[i], save_path)
