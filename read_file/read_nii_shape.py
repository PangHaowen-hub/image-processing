import SimpleITK as sitk
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'E:\ISICDM2023\data\glioma_sgementation\imageTr'

    img = get_listdir(img_path)
    img.sort()

    for i in img:
        sitk_img = sitk.ReadImage(i)
        img_arr = sitk.GetArrayFromImage(sitk_img)
        img_spa = sitk_img.GetSpacing()
        print(i)
        print(img_arr.shape)
        print(img_spa)

