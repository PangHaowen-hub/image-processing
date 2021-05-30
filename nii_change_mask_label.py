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
    l_mask_sitk_img = sitk.ReadImage(mask)
    l_mask_img_arr = sitk.GetArrayFromImage(l_mask_sitk_img)
    r_mask_sitk_img = sitk.ReadImage(mask)
    r_mask_img_arr = sitk.GetArrayFromImage(r_mask_sitk_img)
    r_mask_img_arr[l_mask_img_arr == 5] = 4
    new_mask_img = sitk.GetImageFromArray(r_mask_img_arr)
    new_mask_img.SetDirection(r_mask_sitk_img.GetDirection())
    new_mask_img.SetOrigin(r_mask_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(r_mask_sitk_img.GetSpacing())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, path + fullflname)


if __name__ == '__main__':
    mask_path = r'F:\my_lobe_data\after\_SJ_test\LL\predict_lobe'
    save_path = r'F:\my_lobe_data\after\_SJ_test\LL\predict_final/'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        add_label(mask[i], save_path)
