import SimpleITK as sitk
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def transpose(mask, path):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    direction = (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, -1.0)
    new_mask_img.SetDirection(direction)
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, path + fullflname)


if __name__ == '__main__':
    mask_path = r'F:\LOLA11\lola11_nii'
    save_path = 'F:/LOLA11/lola11_nii_t/'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        transpose(mask[i], save_path)
