import numpy as np
import SimpleITK as sitk

data = np.load(r'C:\Users\Administrator\Desktop\lobe_004.npz')
x = data['data'].astype(int)
x0 = x[0, :, :, :]
x1 = x[1, :, :, :]

print(x.shape)

# mask_sitk_img = sitk.ReadImage(r'F:\my_lobe_data\before\all_lobe_512\imgs\caohongxiang_before.nii.gz')

new_mask_img = sitk.GetImageFromArray(x1)
new_mask_img.SetSpacing((0.8, 0.8, 0.8))
# new_mask_img.SetDirection(mask_sitk_img.GetDirection())
# new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
sitk.WriteImage(new_mask_img, r'C:\Users\Administrator\Desktop\lobe_004_x1.npz.nii.gz')
