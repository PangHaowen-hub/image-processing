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


def add_label(mask, path):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    temp = copy.deepcopy(mask_img_arr)  # 深拷贝
    mask_img_arr[temp == 3] = 1
    mask_img_arr[temp == 4] = 2
    mask_img_arr[temp == 1] = 3
    mask_img_arr[temp == 6] = 4
    mask_img_arr[temp == 2] = 5
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, path + fullflname)


if __name__ == '__main__':
    mask_path = r'F:\lobe\lobe_data_lobe\RU_final\before\mask'
    save_path = 'F:/my_lobe_data/before/RU/masks/'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        add_label(mask[i], save_path)
