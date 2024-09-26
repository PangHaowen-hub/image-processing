import os
import nibabel as nib
import numpy as np


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list



if __name__ == '__main__':
    img_path = r'C:\Users\40702\Desktop'
    nii_list = get_listdir(img_path)
    nii_list.sort()
    orientations = []
    for n in nii_list:
        img = nib.load(n)
        affine = img.affine
        orientation = nib.aff2axcodes(affine)
        print(n)
        print(orientation)
        orientations.append(orientation)
    # orientations = np.array(orientations)
    # unique_orientations = np.unique(orientations, axis=0)
    # all_same = len(unique_orientations) == 1
    # print(all_same, unique_orientations)
