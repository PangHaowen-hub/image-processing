import SimpleITK as sitk
import os
import copy


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def read_nii(mask1, mask2):
    mask_sitk_img1 = sitk.ReadImage(mask1)
    mask_img_arr1 = sitk.GetArrayFromImage(mask_sitk_img1)
    mask_sitk_img2 = sitk.ReadImage(mask2)
    mask_img_arr2 = sitk.GetArrayFromImage(mask_sitk_img2)
    x = mask_sitk_img2.GetDirection()
    print(mask_img_arr1.shape)
    print(mask_img_arr2.shape)



if __name__ == '__main__':
    mask_path = r'F:\lobe\lobe_data_lobe\RL_final\before\mask'
    mask2_path = r'F:\my_lobe_data\before\RL\masks'

    mask = get_listdir(mask_path)
    mask.sort()
    mask2 = get_listdir(mask2_path)
    mask2.sort()
    for i in range(len(mask)):
        read_nii(mask[i], mask2[i])