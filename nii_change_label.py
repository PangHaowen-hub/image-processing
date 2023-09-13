import SimpleITK as sitk
import os
import copy
import tqdm


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def change_label(mask, save_path):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    temp = copy.deepcopy(mask_img_arr)
    mask_img_arr[temp != 0] = 1000
    mask_img_arr[temp == 0] = -1000

    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(mask_sitk_img.GetDirection())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    mask_path = r'\\d204\COPD-Group\BBE-Revise\temp'
    save_path = r'\\d204\COPD-Group\BBE-Revise\temp2'
    mask_list = get_listdir(mask_path)
    mask_list.sort()
    for i in tqdm.tqdm(mask_list):
        change_label(i, save_path)