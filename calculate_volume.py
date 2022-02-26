import SimpleITK as sitk
import os
import tqdm
import collections
import xlwt


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def volume(mask):
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)
    Spacing = mask_sitk_img.GetSpacing()
    # voxel_volume = Spacing[0] * Spacing[1] * Spacing[2]
    lobe_count = collections.Counter(mask_img_arr.flatten())
    # lobe1 = lobe_count[1] * voxel_volume
    # lobe2 = lobe_count[2] * voxel_volume
    # lobe3 = lobe_count[3] * voxel_volume
    # lobe4 = lobe_count[4] * voxel_volume
    # lobe5 = lobe_count[5] * voxel_volume
    # return lobe1, lobe2, lobe3, lobe4, lobe5

    return lobe_count[1], lobe_count[2], lobe_count[3], lobe_count[4], lobe_count[5],


if __name__ == '__main__':
    mask_path = r'H:\my_lobe_data\lobectomy_classification\shengjing_mask\after'
    mask_list = get_listdir(mask_path)
    mask_list.sort()
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
    worksheet = workbook.add_sheet('after_SJ')  # 创建一个worksheet
    for i in tqdm.trange(len(mask_list)):
        lobe1, lobe2, lobe3, lobe4, lobe5 = volume(mask_list[i])

        worksheet.write(i, 0, label=mask_list[i])  # 参数对应 行, 列, 值
        worksheet.write(i, 1, label=lobe1)
        worksheet.write(i, 2, label=lobe2)
        worksheet.write(i, 3, label=lobe3)
        worksheet.write(i, 4, label=lobe4)
        worksheet.write(i, 5, label=lobe5)

    workbook.save(r'H:\my_lobe_data\lobectomy_classification\after_SJ.xls')  # 保存
