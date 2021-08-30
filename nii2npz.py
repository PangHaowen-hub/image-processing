import numpy as np
import SimpleITK as sitk

sitk_img = sitk.ReadImage(r'D:\github_code\Airway-master\example_data\my_data\airway_mask_resample.nii.gz')
img_arr = sitk.GetArrayFromImage(sitk_img)
img_arr = np.flip(img_arr, axis=0)
# img_arr = np.flip(img_arr, axis=1)
# img_arr = np.flip(img_arr, axis=2)
np.savez(r"D:\github_code\Airway-master\example_data\model2.npz", img_arr)
