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
    img_path = r'G:\stroke2022\MICCAI_Stroke_2022\FLAIR'

    img = get_listdir(img_path)
    img.sort()
    shape0 = []
    shape1 = []
    shape2 = []

    # Spacing = []
    for i in range(len(img)):
        sitk_img = sitk.ReadImage(img[i])
        img_arr = sitk.GetArrayFromImage(sitk_img)
        # Spacing.append(sitk_img.GetSpacing())
        shape0.append(img_arr.shape[0])
        shape1.append(img_arr.shape[1])
        shape2.append(img_arr.shape[2])

    shape0.sort()
    shape1.sort()
    shape2.sort()
    print(shape0[249])
    print(shape1[249])
    print(shape2[249])