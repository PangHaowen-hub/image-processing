import SimpleITK as sitk
import os
import copy


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
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
    mask_img_arr[temp != 0] = 0
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, path + fullflname)


# 将肺叶合并成肺区
if __name__ == '__main__':
    mask_path = r'C:\Users\Administrator\Desktop\RU\mask'
    save_path = r'C:\Users\Administrator\Desktop\RU\mask/'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        add_label(mask[i], save_path)
