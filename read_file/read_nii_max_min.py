import SimpleITK as sitk
import os
import numpy as np
from tqdm import trange


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'D:\my_code\Federated_Learning\Flower_NC2CE\data\ZYJ_AH_25'

    img = os.listdir(img_path)
    img.sort()
    min_list = []
    max_list = []

    # Spacing = []
    for i in trange(len(img)):
        sitk_img = sitk.ReadImage(os.path.join(img_path, img[i], 'T1_0_dose.nii.gz'))
        img_arr = sitk.GetArrayFromImage(sitk_img)
        min_list.append(np.min(img_arr))
        max_list.append(np.max(img_arr))

    min_list.sort()
    max_list.sort()

    print(min_list)
    print(max_list)
