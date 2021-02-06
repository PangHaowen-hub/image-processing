import SimpleITK as sitk
import os


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(l_mask, r_mask, add_mask_path):
    l_mask_sitk_img = sitk.ReadImage(l_mask)
    l_mask_img_arr = sitk.GetArrayFromImage(l_mask_sitk_img)
    r_mask_sitk_img = sitk.ReadImage(r_mask)
    r_mask_img_arr = sitk.GetArrayFromImage(r_mask_sitk_img)
    r_mask_img_arr[l_mask_img_arr == 4] = 4
    r_mask_img_arr[l_mask_img_arr == 5] = 5
    new_mask_img = sitk.GetImageFromArray(r_mask_img_arr)
    _, fullflname = os.path.split(l_mask)
    sitk.WriteImage(new_mask_img, add_mask_path + fullflname)


if __name__ == '__main__':
    l_mask_path = r'F:\my_lobe_data\after\RL\delete_right_predict'
    r_mask_path = r'F:\my_lobe_data\after\RL\delete_left_predict'
    add_mask_path = 'F:/my_lobe_data/after/RL/add_left_right'
    l_mask = get_listdir(l_mask_path)
    l_mask.sort()
    r_mask = get_listdir(r_mask_path)
    r_mask.sort()
    for i in range(len(l_mask)):
        add_label(l_mask[i], r_mask[i], add_mask_path)
