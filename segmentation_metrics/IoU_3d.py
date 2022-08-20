import SimpleITK as sitk
import numpy as np
import os
from tqdm import trange


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def iou_3d(mask_path, pred_path, label):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    pred_sitk_img = sitk.ReadImage(pred_path)
    pred_img_arr = sitk.GetArrayFromImage(pred_sitk_img)
    pred_img_arr = pred_img_arr.astype(np.uint16)

    mask_img_arr[mask_img_arr != label] = 0
    mask_img_arr[mask_img_arr == label] = 1
    pred_img_arr[pred_img_arr != label] = 0
    pred_img_arr[pred_img_arr == label] = 1

    intersection = np.sum(mask_img_arr * pred_img_arr)
    y_o = np.sum(mask_img_arr)
    y_pred_o = np.sum(pred_img_arr)
    union = y_o + y_pred_o - intersection

    iou = intersection / union
    print(iou)
    return iou


if __name__ == '__main__':
    mask_path = r'F:\my_code\NCCT2CECT\pix2pix-3d-ncct2cect\2022-06-04-21-12-11\segmentation_test\ISICDM2021\mask'
    pred_path = r'F:\my_code\NCCT2CECT\pix2pix-3d-cect2ncct\2022-06-09-17-22-11\nnunet_test'
    mask = get_listdir(mask_path)
    mask.sort()
    pred = get_listdir(pred_path)
    pred.sort()
    IoU = 0
    for i in trange(len(mask)):
        IoU += iou_3d(mask[i], pred[i], 1)
    print(IoU / len(mask))
