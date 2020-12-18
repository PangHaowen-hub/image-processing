import nibabel as nib
import numpy as np

pred = 'D:/github_code/nnUNet/pred_pred_unpostprocessing/lobe_075.nii.gz'
true = 'D:/github_code/nnUNet/pred_pred_unpostprocessing/lobe_075.nii.gz'

img_pred = nib.load(pred)
y_pred = img_pred.get_fdata()
img_true = nib.load(true)
y_true = img_true.get_fdata()

pred = np.asarray(y_pred).astype(np.int)
print(pred.shape)
true = np.asarray(y_true).astype(np.int)
print(true.shape)
dice1 = 0
dice2 = 0
dice3 = 0
dice4 = 0
dice5 = 0
for i in range(pred.shape[0]):
    for j in range(pred.shape[1]):
        for k in range(pred.shape[2]):
            if pred[i, j, k] == true[i, j, k]:
                if true[i, j, k] == 1:
                    dice1 = dice1 + 1
                elif true[i, j, k] == 2:
                    dice2 = dice2 + 1
                elif true[i, j, k] == 3:
                    dice3 = dice3 + 1
                elif true[i, j, k] == 4:
                    dice4 = dice4 + 1
                elif true[i, j, k] == 5:
                    dice5 = dice5 + 1

sum1 = sum(pred == 1) + sum(true == 1)
sum2 = sum(pred == 2) + sum(true == 2)
sum3 = sum(pred == 3) + sum(true == 3)
sum4 = sum(pred == 4) + sum(true == 4)
sum5 = sum(pred == 5) + sum(true == 5)
# edice1 = 2 * dice1 / sum1
# edice2 = 2 * dice2 / sum2
# edice3 = 2 * dice3 / sum3
# edice4 = 2 * dice4 / sum4
# edice5 = 2 * dice5 / sum5
#
# print(dice1)
# print(dice2)
# print(dice3)
# print(dice4)
# print(dice5)
