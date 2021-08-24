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


def add_label(mask, path):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    b = copy.deepcopy(mask_img_arr)
    mask_img_arr[b == 3] = 1
    mask_img_arr[b == 4] = 2
    mask_img_arr[b == 5] = 3
    mask_img_arr[b == 1] = 4
    mask_img_arr[b == 2] = 5
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(mask_sitk_img.GetDirection())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, os.path.join(path, fullflname))


if __name__ == '__main__':
    mask_path = r'F:\my_lobe_data\before\_LUNA16_test\lungmask_predict'
    save_path = r'F:\my_lobe_data\before\_LUNA16_test\lungmask_predict_temp'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        add_label(mask[i], save_path)
