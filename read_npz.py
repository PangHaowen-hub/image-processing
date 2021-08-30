import numpy as np
import SimpleITK as sitk


data = np.load(r'D:\github_code\Airway-master\example_data\model2.npz')
x = data['arr_0'].astype(int)
print(x.shape)

# mask_sitk_img = sitk.ReadImage(r'F:\my_lobe_data\before\all_lobe_512\imgs\caohongxiang_before.nii.gz')

new_mask_img = sitk.GetImageFromArray(x)
new_mask_img.SetSpacing((0.8, 0.8, 0.8))
# new_mask_img.SetDirection(mask_sitk_img.GetDirection())
# new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
sitk.WriteImage(new_mask_img, r'D:\github_code\Airway-master\example_data\temp2.nii.gz')
