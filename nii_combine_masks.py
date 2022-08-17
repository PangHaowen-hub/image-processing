import os
import tqdm
import SimpleITK as sitk
import numpy as np

def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == "__main__":
    image_path = r'G:\TotalSegmentator\test.nii.gz'
    input_path = r'G:\TotalSegmentator\segmentations'
    output_path = r'G:\TotalSegmentator\segmentations.nii.gz'
    mask_list = get_listdir(input_path)
    num = 1
    sitk_img_0 = sitk.ReadImage(image_path)
    img_arr_total = sitk.GetArrayFromImage(sitk_img_0)
    img_arr_total[img_arr_total != 0] = 0
    for mask in tqdm.tqdm(mask_list):
        sitk_img = sitk.ReadImage(mask)
        img_arr = sitk.GetArrayFromImage(sitk_img)
        img_arr_total[img_arr == 1] = num
        num += 1
    img_arr_total = np.flip(img_arr_total, axis=1)
    img_arr_total = np.flip(img_arr_total, axis=2)
    new_mask_img = sitk.GetImageFromArray(img_arr_total)
    new_mask_img.SetDirection(sitk_img_0.GetDirection())
    new_mask_img.SetOrigin(sitk_img_0.GetOrigin())
    new_mask_img.SetSpacing(sitk_img_0.GetSpacing())
    sitk.WriteImage(new_mask_img, output_path)
