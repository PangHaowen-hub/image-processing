import SimpleITK as sitk
import os
import numpy as np
img_path = r'D:\my_code\airway_segmentation\1234567\img.nii.gz'
mask_path = r'D:\my_code\airway_segmentation\1234567\lobe_mask.nii.gz'
save_path = r'D:\my_code\segment_registration\img_RL.nii.gz'


mask_sitk = sitk.ReadImage(mask_path)
mask_arr = sitk.GetArrayFromImage(mask_sitk)
img_sitk = sitk.ReadImage(img_path)
img_arr = sitk.GetArrayFromImage(img_sitk)
img_arr[mask_arr != 3] = 0
print(img_arr.shape, end=" ")
for axis in [0, 1, 2]:
    sums = np.sum(np.sum(img_arr, axis=axis), axis=(axis + 1) % 2)

    # Track all =0 layers from front from that axis
    remove_front_index = 0
    while sums[remove_front_index] == 0:
        remove_front_index += 1

    # Track all =0 layers from back from that axis
    remove_back_index = len(sums) - 1
    while sums[remove_back_index] == 0:
        remove_back_index -= 1

    # Remove those layers
    img_arr = np.delete(
        img_arr, list(range(remove_front_index - 1)) + list(range(remove_back_index + 2, len(sums))),
        axis=(axis + 1) % 3
    )
    validation_sums = np.sum(np.sum(img_arr, axis=axis), axis=(axis + 1) % 2)
    print(" -> ", img_arr.shape, end=" ")

new_mask_img = sitk.GetImageFromArray(img_arr)
new_mask_img.SetDirection(img_sitk.GetDirection())
new_mask_img.SetOrigin(img_sitk.GetOrigin())
new_mask_img.SetSpacing(img_sitk.GetSpacing())
sitk.WriteImage(new_mask_img, save_path)
