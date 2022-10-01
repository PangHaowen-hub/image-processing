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


def SP_3d(mask_path, pred_path, label):
    mask_sitk_img = sitk.ReadImage(mask_path)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    pred_sitk_img = sitk.ReadImage(pred_path)
    pred_img_arr = sitk.GetArrayFromImage(pred_sitk_img)
    pred_img_arr = pred_img_arr.astype(np.uint16)

    mask_img_arr[mask_img_arr != label] = 0
    mask_img_arr[mask_img_arr == label] = 1
    pred_img_arr[pred_img_arr != label] = 0
    pred_img_arr[pred_img_arr == label] = 1

    TP = np.sum(mask_img_arr * pred_img_arr)

    temp = pred_img_arr - mask_img_arr
    temp[temp == -1] = 0
    FP = np.sum(temp)

    num = mask_img_arr.size
    RealP = np.sum(mask_img_arr)
    RealN = num - RealP

    PredP = np.sum(pred_img_arr)
    PredN = num - PredP

    TPR = TP / RealP
    FPR = FP / RealN

    print(TPR)
    print(FPR)

    return TPR, FPR


if __name__ == '__main__':
    mask_path = r'F:\my_code\NCCT2CECT\figure\fig9\gt\mask'
    pred_path = r'F:\my_code\NCCT2CECT\figure\fig9\ncct-ncct\pred_CoTr'

    mask = get_listdir(mask_path)
    mask.sort()
    pred = get_listdir(pred_path)
    pred.sort()
    TPR = 0
    FPR = 0
    for i in trange(len(mask)):
        temp = SP_3d(mask[i], pred[i], 1)
        TPR += temp[0]
        FPR += temp[1]

    print('TPR:', TPR / len(mask))
    print('FPR:', FPR / len(mask))
