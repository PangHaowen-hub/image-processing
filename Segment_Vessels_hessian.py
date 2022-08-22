import os
import itk
from distutils.version import StrictVersion as VS
import sys

import tqdm

if VS(itk.Version.GetITKVersion()) < VS("5.0.0"):
    print("ITK 5.0.0 or newer is required.")
    sys.exit(1)


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def hessian(input_path, save_path):
    sigma = 1.0
    alpha1 = 0.5
    alpha2 = 2.0
    input_image = itk.imread(input_path, itk.ctype("float"))
    hessian_image = itk.hessian_recursive_gaussian_image_filter(input_image, sigma=sigma)
    vesselness_filter = itk.Hessian3DToVesselnessMeasureImageFilter[itk.ctype("float")].New()
    vesselness_filter.SetInput(hessian_image)
    vesselness_filter.SetAlpha1(alpha1)
    vesselness_filter.SetAlpha2(alpha2)

    _, fullflname = os.path.split(input_path)
    itk.imwrite(vesselness_filter, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    input_image = r'F:\my_code\NCCT2CECT\pix2pix-3d-cect2ncct\2022-06-09-17-22-11\nnunet_test\luzong\image'
    output_image = r'F:\my_code\NCCT2CECT\pix2pix-3d-cect2ncct\2022-06-09-17-22-11\nnunet_test\luzong\pred_hessian'
    img_list = get_listdir(input_image)
    img_list.sort()
    for i in tqdm.trange(len(img_list)):
        hessian(img_list[i], output_image)
