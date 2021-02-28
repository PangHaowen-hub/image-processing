import SimpleITK as sitk
import numpy as np
import os


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def dice_3d(mask_path, pred_path):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    pred_sitk_img = sitk.ReadImage(pred_path)
    pred_img_arr = sitk.GetArrayFromImage(pred_sitk_img)
    pred_img_arr = pred_img_arr.astype(np.uint16)
    # 求不同的肺叶dice修改此处
    mask_img_arr[mask_img_arr != 5] = 0
    mask_img_arr[mask_img_arr == 5] = 1
    pred_img_arr[pred_img_arr != 5] = 0
    pred_img_arr[pred_img_arr == 5] = 1

    denominator = np.sum(mask_img_arr) + np.sum(pred_img_arr)
    numerator = 2 * np.sum(mask_img_arr * pred_img_arr)
    dice = numerator / denominator
    print(dice)


if __name__ == '__main__':
    mask_path = r'F:\my_lobe_data\after\RU\test_mask'
    pred_path = r'F:\my_lobe_data\after\RU\_final_predict'
    mask = get_listdir(mask_path)
    mask.sort()
    pred = get_listdir(pred_path)
    pred.sort()
    for i in range(len(mask)):
        dice_3d(mask[i], pred[i])
