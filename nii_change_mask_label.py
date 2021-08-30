import SimpleITK as sitk
import os
import copy


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(mask1, mask2, path):
    mask_sitk_img1 = sitk.ReadImage(mask1)
    mask_sitk_img2 = sitk.ReadImage(mask2)

    mask_img_arr1 = sitk.GetArrayFromImage(mask_sitk_img1)
    mask_img_arr2 = sitk.GetArrayFromImage(mask_sitk_img2)

    a = copy.deepcopy(mask_img_arr1)
    b = copy.deepcopy(mask_img_arr2)
    mask_img_arr1[a == 1] = 6
    mask_img_arr1[a == 2] = 5
    mask_img_arr1[a == 3] = 4
    mask_img_arr1[a == 4] = 3
    mask_img_arr1[a == 5] = 2
    mask_img_arr1[b == 1] = 1

    new_mask_img = sitk.GetImageFromArray(mask_img_arr1)
    new_mask_img.SetDirection(mask_sitk_img1.GetDirection())
    new_mask_img.SetOrigin(mask_sitk_img1.GetOrigin())
    new_mask_img.SetSpacing(mask_sitk_img1.GetSpacing())
    sitk.WriteImage(new_mask_img, path)


if __name__ == '__main__':
    mask_path_1 = r'D:\github_code\Airway-master\example_data\my_data\lobe_mask_resample.nii.gz'
    mask_path_2 = r'D:\github_code\Airway-master\example_data\my_data\airway_mask_resample.nii.gz'
    save_path = r'D:\github_code\Airway-master\example_data\my_data\lobe_airway_mask_resample.nii.gz'
    add_label(mask_path_1, mask_path_2, save_path)
