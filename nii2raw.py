import SimpleITK
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.gz'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def nii_raw(mask, path):
    mask_sitk_img = SimpleITK.ReadImage(mask)
    mask_img_arr = SimpleITK.GetArrayFromImage(mask_sitk_img)
    new_mask_img = SimpleITK.GetImageFromArray(mask_img_arr)
    new_mask_img.SetSpacing(mask_sitk_img.GetSpacing())
    new_mask_img.SetOrigin(mask_sitk_img.GetOrigin())
    new_mask_img.SetDirection(mask_sitk_img.GetDirection())
    _, fullflname = os.path.split(mask)
    SimpleITK.WriteImage(new_mask_img, path + fullflname[:-7] + ".mhd")


if __name__ == '__main__':
    mask_path = r'C:\Users\Administrator\Desktop\temp'
    save_path = 'C:/Users/Administrator/Desktop/temp/'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        nii_raw(mask[i], save_path)






