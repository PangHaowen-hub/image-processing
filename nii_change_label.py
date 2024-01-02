import SimpleITK as sitk
import os
import copy
import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def change_label(mask):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)

    mask_img_arr[mask_img_arr != 0] = 1

    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.CopyInformation(mask_sitk_img)
    sitk.WriteImage(new_mask_img, mask)


if __name__ == '__main__':
    mask_path = r'D:\my_code\Federated_Learning\FL-NC2CE\data\origin_ZYJ_inter_25_seg_mask'
    mask_list = get_listdir(mask_path)
    mask_list.sort()
    for mask_name in tqdm.tqdm(mask_list):
        change_label(mask_name)
