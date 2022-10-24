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
    img_path = r'H:\CT2CECT\gz_DECT\AA'

    img = get_listdir(img_path)
    img.sort()
    shape = 0
    for i in range(len(img)):
        sitk_img = sitk.ReadImage(img[i])
        img_arr = sitk.GetArrayFromImage(sitk_img)
        shape += img_arr.shape[0]
    print(shape)