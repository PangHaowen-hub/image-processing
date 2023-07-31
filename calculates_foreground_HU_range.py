import SimpleITK as sitk
import os
from tqdm import trange


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def HU(image, mask):
    image_sitk = sitk.ReadImage(image)
    image_arr = sitk.GetArrayFromImage(image_sitk)
    mask_sitk = sitk.ReadImage(mask)
    mask_arr = sitk.GetArrayFromImage(mask_sitk)

    print(max(image_arr[mask_arr != 0]))
    print(min(image_arr[mask_arr != 0]))


if __name__ == '__main__':
    image_path = r'H:\CT2CECT\segmentation\wmh_vessel\img'
    mask_path = r'H:\CT2CECT\segmentation\wmh_vessel\mask'

    image = get_listdir(image_path)
    image.sort()

    mask = get_listdir(mask_path)
    mask.sort()
    for i in trange(len(image)):
        HU(image[i], mask[i])
