from tqdm import tqdm
import os
import SimpleITK as sitk


def read_txt(txt):
    name_list = []
    with open(txt, "r") as f:
        for line in f.readlines():
            name_list.append('.' + line.strip('\n'))  # 去掉列表中每一个元素的换行符
    return name_list


def load_data():
    train_txt = '../data/train_all.txt'
    val_txt = '../data/val_all.txt'
    test_txt = '../data/test_all.txt'
    name_list_train = read_txt(train_txt)
    name_list_val = read_txt(val_txt)
    name_list_test = read_txt(test_txt)
    name_list_all = name_list_train + name_list_val + name_list_test
    name_list_all.sort()
    train_0_paths = [os.path.join(i, 'T1_0_dose_Harm_diff_2_5.nii.gz') for i in name_list_all]

    subjects_train = []
    for train_0_path in train_0_paths:
        subject = dict(T1_0=train_0_path)
        subjects_train.append(subject)

    return subjects_train


if __name__ == '__main__':
    trainloader = load_data()

    for images in tqdm(trainloader):
        image_0 = sitk.ReadImage(images['T1_0'], sitk.sitkUInt8)
        dilate_filter = sitk.BinaryMorphologicalOpeningImageFilter()
        dilate_filter.SetKernelRadius(1)
        output_image = dilate_filter.Execute(image_0)

        sitk.WriteImage(output_image, os.path.join(os.path.split(images['T1_0'])[0], 'T1_0_dose_Harm_diff_2_5_open.nii.gz'))

