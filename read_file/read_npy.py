import numpy as np
import SimpleITK as sitk

data = np.load(r'C:\Users\Administrator\Desktop\lobe_000.npy')
x0 = data[0, :, :, :]
x1 = data[1, :, :, :]

new_mask_img0 = sitk.GetImageFromArray(x0)
new_mask_img0.SetSpacing((0.8, 0.8, 0.8))
sitk.WriteImage(new_mask_img0, r'C:\Users\Administrator\Desktop\lobe_000_x0.npy.nii.gz')

new_mask_img1 = sitk.GetImageFromArray(x1)
new_mask_img1.SetSpacing((0.8, 0.8, 0.8))
sitk.WriteImage(new_mask_img1, r'C:\Users\Administrator\Desktop\lobe_000_x1.npy.nii.gz')
