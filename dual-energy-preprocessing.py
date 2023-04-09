import SimpleITK as sitk

low = r'G:\Dual-energyCT\DICOMO\PA0\ST0\SE3.nii.gz'
high = r'G:\Dual-energyCT\DICOMO\PA0\ST0\SE5.nii.gz'

low_sitk_img = sitk.ReadImage(low)
low_img_arr = sitk.GetArrayFromImage(low_sitk_img)
high_sitk_img = sitk.ReadImage(high)
high_img_arr = sitk.GetArrayFromImage(high_sitk_img)

temp = (low_img_arr - high_img_arr) / (low_img_arr + high_img_arr + 2000)

new_img = sitk.GetImageFromArray(temp)
new_img.SetDirection(low_sitk_img.GetDirection())
new_img.SetOrigin(low_sitk_img.GetOrigin())
new_img.SetSpacing(low_sitk_img.GetSpacing())
sitk.WriteImage(new_img, r'G:\Dual-energyCT\DICOMO\PA0\ST0\SE3-5.nii.gz')
