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


def add_label(mask):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    temp = copy.deepcopy(mask_img_arr)
    mask_img_arr[temp == 2] = 3

    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(mask_sitk_img.GetDirection())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    sitk.WriteImage(new_mask_img, mask)


if __name__ == '__main__':
    mask_path = r'F:\my_lobe_data\after\RM\masks_UNet_pred\_right_predict'
    mask_list = get_listdir(mask_path)
    for i in mask_list:
        add_label(i)
