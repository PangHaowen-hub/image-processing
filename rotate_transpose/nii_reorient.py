import os
from nipype.interfaces import fsl
import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def reorient(path):
    MNI = fsl.Reorient2Std()
    MNI.inputs.in_file = path
    MNI.inputs.out_file = path
    MNI_results = MNI.run()
    return MNI_results


if __name__ == '__main__':
    data_root = '../data/ZYJ_AH_25_zscore_based_on_T1'
    name_list = [os.path.join(data_root, i) for i in os.listdir(data_root)]
    name_list.sort()
    for i in tqdm.tqdm(name_list):
        try:
            reorient(os.path.join(i, 'T1_0_dose.nii.gz'))
            reorient(os.path.join(i, 'T1_25_dose.nii.gz'))
            reorient(os.path.join(i, 'T1_100_dose.nii.gz'))
        except Exception as e:
            print(e)
            print('Fail!')
