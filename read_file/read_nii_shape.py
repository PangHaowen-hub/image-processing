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
    img_path = r'E:\Federated_Learning\FL-DA\data\ZYJ_inter_25_zscore_based_on_T1'

    img = os.listdir(img_path)
    img.sort()

    for i in range(len(img)):
        sitk_img = sitk.ReadImage(os.path.join(img_path, img[i], 'T1_0_dose.nii.gz'))
        img_arr = sitk.GetArrayFromImage(sitk_img)
        print(img_arr.shape)
