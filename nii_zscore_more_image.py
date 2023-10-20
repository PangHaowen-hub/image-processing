import numpy as np
import SimpleITK as sitk


if __name__ == '__main__':
    t1_0_path = r'C:\Users\40702\Desktop\T1_0_dose.nii.gz'
    t1_low_path = r'C:\Users\40702\Desktop\T1_25_dose.nii.gz'
    t1_100_path = r'C:\Users\40702\Desktop\T1_100_dose.nii.gz'

    save_path = r'C:\Users\40702\Desktop\temp'

    t1_0_img = sitk.ReadImage(t1_0_path)
    t1_low_img = sitk.ReadImage(t1_low_path)
    t1_100_img = sitk.ReadImage(t1_100_path)

    t1_0_arr = sitk.GetArrayFromImage(t1_0_img)
    t1_low_arr = sitk.GetArrayFromImage(t1_low_img)
    t1_100_arr = sitk.GetArrayFromImage(t1_100_img)

    new_t1_0 = (t1_0_arr - np.mean(t1_0_arr)) / np.std(t1_0_arr)
    new_t1_low = (t1_low_arr - np.mean(t1_0_arr)) / np.std(t1_0_arr)
    new_t1_100 = (t1_100_arr - np.mean(t1_0_arr)) / np.std(t1_0_arr)

    new_img_t1_0 = sitk.GetImageFromArray(new_t1_0)
    new_img_t1_0.CopyInformation(t1_0_img)

    new_img_t1_low = sitk.GetImageFromArray(new_t1_low)
    new_img_t1_low.CopyInformation(t1_low_img)

    new_img_t1_100 = sitk.GetImageFromArray(new_t1_100)
    new_img_t1_100.CopyInformation(t1_100_img)

    sitk.WriteImage(new_img_t1_0, t1_0_path)
    sitk.WriteImage(new_img_t1_low, t1_low_path)
    sitk.WriteImage(new_img_t1_100, t1_100_path)

