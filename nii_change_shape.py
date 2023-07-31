import os
import SimpleITK as sitk

if __name__ == '__main__':
    img_path = r'H:\CT2CECT\registration\data\cect_a\039.nii.gz'
    save_path = r'C:\Users\user\Desktop'
    sitk_img = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    new_arr = img_arr[20:, :, :]
    new_img = sitk.GetImageFromArray(new_arr)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetOrigin(sitk_img.GetOrigin())
    new_img.SetSpacing(sitk_img.GetSpacing())
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))
