import SimpleITK as sitk
import os
import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'/data7/xinruzhang/DATA/TTCA/ZYJ_20220610-rename-nii-cutneck-rigid-regristrate/ZYJ_inter_25'
    # img_path = r'E:\Federated_Learning\FL-NC2CE\data\origin_ZYJ_AH_25'

    img_list = os.listdir(img_path)
    img_list.sort()
    shape_list = set()
    spa_list = set()

    for i in tqdm.tqdm(img_list):
        sitk_img = sitk.ReadImage(os.path.join(img_path, i, "T1_100_dose.nii.gz"))
        img_arr = sitk.GetArrayFromImage(sitk_img)
        img_spa = sitk_img.GetSpacing()
        shape_list.add(img_arr.shape)
        spa_list.add(img_spa)
    shape_list = list(shape_list)
    shape_list.sort()
    print(shape_list)

    spa_list = list(spa_list)
    spa_list.sort()
    print(spa_list)
