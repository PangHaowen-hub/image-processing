import SimpleITK as sitk
from tqdm import trange
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def subtraction_ct(img1, img2, savepath):
    sitk_img1 = sitk.ReadImage(img1)
    img_arr1 = sitk.GetArrayFromImage(sitk_img1)
    sitk_img2 = sitk.ReadImage(img2)
    img_arr2 = sitk.GetArrayFromImage(sitk_img2)

    img_arr1 = img_arr1 - img_arr2

    new_img = sitk.GetImageFromArray(img_arr1)
    new_img.SetDirection(sitk_img1.GetDirection())
    new_img.SetOrigin(sitk_img1.GetOrigin())
    new_img.SetSpacing(sitk_img1.GetSpacing())
    _, fullflname = os.path.split(img1)
    sitk.WriteImage(new_img, os.path.join(savepath, fullflname))


if __name__ == '__main__':
    CECT_path = r'H:\CT2CECT\gz_DECT\AA_lungbox'
    NCCT_path = r'H:\CT2CECT\gz_DECT\VUE_lungbox'
    save_path = r'H:\CT2CECT\gz_DECT\subtraction_ct'
    CECT_list = get_listdir(CECT_path)
    CECT_list.sort()
    NCCT_list = get_listdir(NCCT_path)
    NCCT_list.sort()
    for i in trange(len(CECT_list)):
        subtraction_ct(CECT_list[i], NCCT_list[i], save_path)
