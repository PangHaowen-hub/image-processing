import SimpleITK as sitk
import os
import tqdm
import numpy as np
import collections
import xlwt
import copy


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def volume(img, mask):
    img_sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(img_sitk_img)
    mask_sitk_img = sitk.ReadImage(mask)
    mask_arr = sitk.GetArrayFromImage(mask_sitk_img)
    Spacing = img_sitk_img.GetSpacing()
    voxel_volume = Spacing[0] * Spacing[1] * Spacing[2]

    save_arr = np.zeros_like(img_arr)
    save_arr[img_arr <= -951] = 1  # 低密度
    temp = np.zeros_like(img_arr)
    temp[img_arr > -950] += 1
    temp[img_arr < -701] += 1
    save_arr[temp == 2] = 2  # 中密度
    save_arr[img_arr >= -700] = 3  # 高密度

    lobe1 = copy.deepcopy(save_arr)
    lobe1[mask_arr != 1] = 0
    lobe2 = copy.deepcopy(save_arr)
    lobe2[mask_arr != 2] = 0
    lobe3 = copy.deepcopy(save_arr)
    lobe3[mask_arr != 3] = 0
    lobe4 = copy.deepcopy(save_arr)
    lobe4[mask_arr != 4] = 0
    lobe5 = copy.deepcopy(save_arr)
    lobe5[mask_arr != 5] = 0

    lobe_count1 = collections.Counter(lobe1.flatten())
    lobe1_volume_1 = lobe_count1[1] * voxel_volume
    lobe1_volume_2 = lobe_count1[2] * voxel_volume
    lobe1_volume_3 = lobe_count1[3] * voxel_volume

    lobe_count2 = collections.Counter(lobe2.flatten())
    lobe2_volume_1 = lobe_count2[1] * voxel_volume
    lobe2_volume_2 = lobe_count2[2] * voxel_volume
    lobe2_volume_3 = lobe_count2[3] * voxel_volume

    lobe_count3 = collections.Counter(lobe3.flatten())
    lobe3_volume_1 = lobe_count3[1] * voxel_volume
    lobe3_volume_2 = lobe_count3[2] * voxel_volume
    lobe3_volume_3 = lobe_count3[3] * voxel_volume

    lobe_count4 = collections.Counter(lobe4.flatten())
    lobe4_volume_1 = lobe_count4[1] * voxel_volume
    lobe4_volume_2 = lobe_count4[2] * voxel_volume
    lobe4_volume_3 = lobe_count4[3] * voxel_volume

    lobe_count5 = collections.Counter(lobe5.flatten())
    lobe5_volume_1 = lobe_count5[1] * voxel_volume
    lobe5_volume_2 = lobe_count5[2] * voxel_volume
    lobe5_volume_3 = lobe_count5[3] * voxel_volume

    return [lobe1_volume_1, lobe1_volume_2, lobe1_volume_3, lobe2_volume_1, lobe2_volume_2, lobe2_volume_3,
            lobe3_volume_1, lobe3_volume_2, lobe3_volume_3, lobe4_volume_1, lobe4_volume_2, lobe4_volume_3,
            lobe5_volume_1, lobe5_volume_2, lobe5_volume_3]


if __name__ == '__main__':
    img_path = r'G:\Lobectomy\shengjing\RUL_nii\before_rename'
    mask_path = r'G:\Lobectomy\shengjing\RUL_nii\RU_before_test_all'
    img_list = get_listdir(img_path)
    mask_list = get_listdir(mask_path)
    img_list.sort()
    mask_list.sort()
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
    worksheet = workbook.add_sheet('RU_before')  # 创建一个worksheet
    for i in tqdm.trange(len(img_list)):
        hu_volume = volume(img_list[i], mask_list[i])
        worksheet.write(i, 0, label=mask_list[i])  # 参数对应 行, 列, 值
        for j in range(15):
            worksheet.write(i, j + 1, label=hu_volume[j])

    workbook.save(r'G:\Lobectomy\shengjing\RUL_nii\RU_before_HU.xls')  # 保存
