import SimpleITK as sitk
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def read_nii(mask1):
    mask_sitk_img1 = sitk.ReadImage(mask1)
    mask_img_arr1 = sitk.GetArrayFromImage(mask_sitk_img1)
    print(mask1)
    print(mask_img_arr1.shape)


if __name__ == '__main__':
    mask_path = r'F:\segment_registration\Registration\original_image\imgs'
    mask = get_listdir(mask_path)
    mask.sort()
    for i in range(len(mask)):
        read_nii(mask[i])
