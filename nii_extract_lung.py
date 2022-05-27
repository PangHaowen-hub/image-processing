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


def add_label(img, mask, savepath):
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    sitk_mask = sitk.ReadImage(mask)
    mask_arr = sitk.GetArrayFromImage(sitk_mask)
    img_arr[mask_arr == 0] = -1000  # TODO:修改此处
    # img_arr[mask_arr == 0] = 0

    new_img = sitk.GetImageFromArray(img_arr)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetOrigin(sitk_img.GetOrigin())
    new_img.SetSpacing(sitk_img.GetSpacing())
    _, fullflname = os.path.split(img)
    sitk.WriteImage(new_img, os.path.join(savepath, fullflname))


if __name__ == '__main__':
    img_path = r'H:\CT2CECT\segmentation\wmh_vessel\img'
    mask_path = r'H:\CT2CECT\segmentation\wmh_vessel\mask'
    save_path = r'H:\CT2CECT\segmentation\wmh_vessel'
    img_list = get_listdir(img_path)
    img_list.sort()
    mask_list = get_listdir(mask_path)
    mask_list.sort()
    for i in trange(len(img_list)):
        add_label(img_list[i], mask_list[i], save_path)
