import SimpleITK as sitk
import numpy as np
import os
from tqdm import trange
from hausdorff import hausdorff_distance

def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def HD_3d(mask_path, pred_path):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    pred_sitk_img = sitk.ReadImage(pred_path)
    pred_img_arr = sitk.GetArrayFromImage(pred_sitk_img)
    pred_img_arr = pred_img_arr.astype(np.uint16)

    mask_index1 = np.argwhere(mask_img_arr == 1)
    mask_index2 = np.argwhere(mask_img_arr == 2)
    mask_index3 = np.argwhere(mask_img_arr == 3)
    mask_index4 = np.argwhere(mask_img_arr == 4)
    mask_index5 = np.argwhere(mask_img_arr == 5)

    pred_index1 = np.argwhere(pred_img_arr == 1)
    pred_index2 = np.argwhere(pred_img_arr == 2)
    pred_index3 = np.argwhere(pred_img_arr == 3)
    pred_index4 = np.argwhere(pred_img_arr == 4)
    pred_index5 = np.argwhere(pred_img_arr == 5)

    hd1 = hausdorff_distance(mask_index1, pred_index1, distance='manhattan')
    hd2 = hausdorff_distance(mask_index2, pred_index2, distance='euclidean')
    hd3 = hausdorff_distance(mask_index3, pred_index3, distance='euclidean')
    hd4 = hausdorff_distance(mask_index4, pred_index4, distance='euclidean')
    hd5 = hausdorff_distance(mask_index5, pred_index5, distance='euclidean')

    return hd1, hd2, hd3, hd4, hd5


if __name__ == '__main__':
    mask_path = r'H:\my_lobe_data\before\all_lobe_512\test_mask\ground_truth'
    pred_path = r'H:\my_lobe_data\before\all_lobe_512\test_mask\test_mask_best'
    mask = get_listdir(mask_path)
    mask.sort()
    pred = get_listdir(pred_path)
    pred.sort()
    HD = 0
    for i in trange(len(mask)):
        HD += HD_3d(mask[i], pred[i])
    print(HD / len(mask))
