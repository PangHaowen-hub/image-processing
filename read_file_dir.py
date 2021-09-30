import os
import SimpleITK as sitk
import shutil
import tqdm
import pypinyin


def dcm_nii(ct_path, save_path, AorB):
    # 读取CT图像
    ct_reader = sitk.ImageSeriesReader()
    dicom_names = ct_reader.GetGDCMSeriesFileNames(ct_path)
    ct_reader.SetFileNames(dicom_names)
    ct_sitk_img = ct_reader.Execute()
    ct_img_arr = sitk.GetArrayFromImage(ct_sitk_img)
    new_mask_img1 = sitk.GetImageFromArray(ct_img_arr)
    new_mask_img1.SetDirection(ct_sitk_img.GetDirection())
    new_mask_img1.SetOrigin(ct_sitk_img.GetOrigin())
    new_mask_img1.SetSpacing(ct_sitk_img.GetSpacing())

    sitk.WriteImage(new_mask_img1, os.path.join(save_path, AorB))


def hp(word):  # 汉字改拼音
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


if __name__ == '__main__':
    path = r'G:\盛京肺叶切除\左下'  # TODO：改此处
    name_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        name_list.append(file_path)
    name_list.sort()
    for i in tqdm.trange(len(name_list)):
        i = name_list[i]
        name = i.split('\\')[-1]
        x1 = os.listdir(os.path.join(i, '术前'))
        x2 = os.listdir(os.path.join(i, '术前', x1[0]))
        for j in x2:
            if j.split('.')[-1] != 'dat':
                dcm_path = os.path.join(i, '术前', x1[0], j)
                shutil.copytree(dcm_path, os.path.join(r"G:\Lobectomy\LLL", hp(name) + '_before'))  # TODO：改此处
        x1 = os.listdir(os.path.join(i, '术后'))
        x2 = os.listdir(os.path.join(i, '术后', x1[0]))
        for j in x2:
            if j.split('.')[-1] != 'dat':
                dcm_path = os.path.join(i, '术后', x1[0], j)
                shutil.copytree(dcm_path, os.path.join(r"G:\Lobectomy\LLL", hp(name) + '_after'))  # TODO：改此处
