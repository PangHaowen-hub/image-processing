import nibabel as nib
import scipy.io as io
import os
import numpy as np
import torch


def dice_coefficient(y_true, y_pred, smooth=0.00001):
    y_true_f = torch.flatten(y_true)
    y_pred_f = torch.flatten(y_pred)
    intersection = torch.sum(y_true_f * y_pred_f)
    return (2. * intersection + smooth) / (torch.sum(y_true_f) + torch.sum(y_pred_f) + smooth)


pred_dir = 'D:/my_code/image-processing/test/1'
true_dir = 'D:/my_code/image-processing/test/2'
pred_filenames = os.listdir(pred_dir)
true_filenames = os.listdir(true_dir)
dice_value = np.zeros(1)
temp = []
for f in range(len(pred_filenames)):
    pred_path = os.path.join(pred_dir, pred_filenames[f])
    true_path = os.path.join(true_dir, true_filenames[f])
    img_pred = nib.load(pred_path)
    img_true = nib.load(true_path)
    y_pred = img_pred.get_fdata()
    y_true = img_true.get_fdata()

    # temp_true1 = y_true
    # temp_true1[y_true != 1] = 0
    # temp_pred1 = y_pred
    # temp_pred1[y_pred != 1] = 0
    # y_pred1 = torch.tensor(temp_pred1)
    # y_true1 = torch.tensor(temp_true1)
    # temp.append(dice_coefficient(y_true1, y_pred1))
    # print(temp)
    #
    temp_true2 = y_true
    temp_true2[y_true != 2] = 0
    temp_true2[y_true == 2] = 1
    temp_pred2 = y_pred
    temp_pred2[y_pred != 2] = 0
    temp_pred2[y_pred == 2] = 1
    y_pred2 = torch.tensor(temp_pred2)
    y_true2 = torch.tensor(temp_true2)

    print(dice_coefficient(y_true2, y_pred2))
    #
    temp_true3 = y_true
    temp_true3[y_true != 3] = 0
    temp_true3[y_true == 3] = 1
    temp_pred3 = y_pred
    temp_pred3[y_pred != 3] = 0
    temp_pred3[y_pred == 3] = 1
    y_pred3 = torch.tensor(temp_pred3)
    y_true3 = torch.tensor(temp_true3)

    print(dice_coefficient(y_true3, y_pred3))
    #
    # temp_true4 = y_true
    # temp_true4[y_true != 4] = 0
    # temp_true4[y_true == 4] = 1
    # temp_pred4 = y_pred
    # temp_pred4[y_pred != 4] = 0
    # temp_pred4[y_pred == 4] = 1
    # y_pred4 = torch.tensor(temp_pred4)
    # y_true4 = torch.tensor(temp_true4)
    # temp.append(dice_coefficient(y_true4, y_pred4))
    # print(temp)
    #
    # temp_true5 = y_true
    # temp_true5[y_true != 5] = 0
    # temp_true5[y_true == 5] = 1
    # temp_pred5 = y_pred
    # temp_pred5[y_pred != 5] = 0
    # temp_pred5[y_pred == 5] = 1
    # y_pred5 = torch.tensor(temp_pred5)
    # y_true5 = torch.tensor(temp_true5)
    # temp.append(dice_coefficient(y_true5, y_pred5))
    # print(temp)
