import SimpleITK as sitk
import os
import copy
import tqdm


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def img_rectity(img, mask, path):
    img_sitk_img = sitk.ReadImage(img)
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)

    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(img_sitk_img.GetDirection())
    new_mask_img.SetOrigin(img_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(img_sitk_img.GetSpacing())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, os.path.join(path, fullflname))


# 修正3d slicer不能读取的mask
if __name__ == '__main__':
    img_path = r'H:\CT2CECT\segmentation\dcm\wmh_vessel\nc\image'  # img路径
    mask_path = r'H:\CT2CECT\segmentation\dcm\wmh_vessel\nc\mask'  # mask路径
    save_path = r'H:\CT2CECT\segmentation\dcm\wmh_vessel\nc\mask1'  # 保存路径
    img = get_listdir(img_path)
    mask = get_listdir(mask_path)
    img.sort()
    mask.sort()
    for i in tqdm.trange(len(mask)):
        img_rectity(img[i], mask[i], save_path)
