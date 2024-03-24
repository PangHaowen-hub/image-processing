import SimpleITK as sitk
import os
import tqdm
import numpy as np

def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    # img_path = r'/data7/xinruzhang/DATA/TTCA/ZYJ_20220610-rename-nii-cutneck-rigid-regristrate/ZYJ_AH_25'
    img_path = r'E:\Federated_Learning\FL-NC2CE\data\origin_ZYJ_inter_25'

    img_list = os.listdir(img_path)
    img_list.sort()
    shape_list_0 = []
    shape_list_1 = []
    shape_list_2 = []

    spa_list_0 = []
    spa_list_1 = []
    spa_list_2 = []


    for i in tqdm.tqdm(img_list):
        sitk_img = sitk.ReadImage(os.path.join(img_path, i, "T1_100_dose.nii.gz"))
        img_arr = sitk.GetArrayFromImage(sitk_img)
        img_spa = sitk_img.GetSpacing()
        shape_list_0.append(img_arr.shape[0])
        shape_list_1.append(img_arr.shape[1])
        shape_list_2.append(img_arr.shape[2])
        spa_list_0.append(img_spa[0])
        spa_list_1.append(img_spa[1])
        spa_list_2.append(img_spa[2])

    print(np.mean(shape_list_0))
    print(np.std(shape_list_0))

    print(np.mean(shape_list_1))
    print(np.std(shape_list_1))

    print(np.mean(shape_list_2))
    print(np.std(shape_list_2))

    print(np.mean(spa_list_0))
    print(np.std(spa_list_0))

    print(np.mean(spa_list_1))
    print(np.std(spa_list_1))

    print(np.mean(spa_list_2))
    print(np.std(spa_list_2))
