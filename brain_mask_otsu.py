import numpy as np
import SimpleITK as sitk


def maxConnectArea(itk_image_):
    """ 获取最大连通域
    return: itk image"""

    cc_filter = sitk.ConnectedComponentImageFilter()
    cc_filter.SetFullyConnected(True)
    output_connected = cc_filter.Execute(itk_image_)
    # -> 0,1,2,....一系列的连通区域编号, 0表示背景
    output_connected_array = sitk.GetArrayFromImage(output_connected)
    # print(np.unique(output_connected_array))
    num_connected_label = cc_filter.GetObjectCount()

    lss_filter = sitk.LabelShapeStatisticsImageFilter()
    lss_filter.Execute(output_connected)

    max_area = 0
    max_label_idx = 0
    # -> 找出最大的area
    # 连通域label从1开始, 0表示背景
    for i in range(1, num_connected_label + 1):
        cur_area = lss_filter.GetNumberOfPixels(i)
        if cur_area > max_area:
            max_area = cur_area
            max_label_idx = i

    re_mask = np.zeros_like(output_connected_array)
    re_mask[output_connected_array == max_label_idx] = 1

    re_image = sitk.GetImageFromArray(re_mask)
    re_image.SetDirection(itk_image_.GetDirection())
    re_image.SetSpacing(itk_image_.GetSpacing())
    re_image.SetOrigin(itk_image_.GetOrigin())
    return re_image


def brain_mask(image_path):
    image_0 = sitk.ReadImage(image_path)

    otsu_filter = sitk.OtsuThresholdImageFilter()
    otsu_filter.SetInsideValue(0)
    otsu_filter.SetOutsideValue(1)
    seg = otsu_filter.Execute(image_0)

    seg = maxConnectArea(seg)  # 取最大联通分量

    dilate_filter = sitk.BinaryMorphologicalClosingImageFilter()
    dilate_filter.SetKernelRadius(30)
    seg = dilate_filter.Execute(seg)

    sitk.WriteImage(seg, image_path[:-7] + '_brain_mask.nii.gz')


if __name__ == '__main__':
    image = r'image.nii.gz'
    brain_mask(image)
