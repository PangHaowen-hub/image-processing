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


def add_label(mask1, mask2, add_mask_path):
    mask1_sitk_img = sitk.ReadImage(mask1)
    mask1_img_arr = sitk.GetArrayFromImage(mask1_sitk_img)
    mask2_sitk_img = sitk.ReadImage(mask2)
    mask2_img_arr = sitk.GetArrayFromImage(mask2_sitk_img)
    mask1_img_arr[mask2_img_arr == 0] = 0
    new_mask_img = sitk.GetImageFromArray(mask1_img_arr)
    new_mask_img.SetDirection(mask1_sitk_img.GetDirection())
    new_mask_img.SetOrigin(mask1_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(mask1_sitk_img.GetSpacing())
    _, fullflname = os.path.split(mask1)
    sitk.WriteImage(new_mask_img, os.path.join(add_mask_path, fullflname))


if __name__ == '__main__':
    mask1_path = r'H:\CT2CECT\segmentation\dcm\wmh_vessel\nc\mask'
    mask2_path = r'H:\CT2CECT\segmentation\dcm\wmh_vessel\nc\image_lungmask'
    save_path = r'H:\CT2CECT\segmentation\dcm\wmh_vessel\nc\mask_new'
    mask1 = get_listdir(mask1_path)
    mask1.sort()
    mask2 = get_listdir(mask2_path)
    mask2.sort()
    for i in trange(len(mask1)):
        add_label(mask1[i], mask2[i], save_path)
