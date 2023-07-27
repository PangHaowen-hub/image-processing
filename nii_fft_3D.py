import SimpleITK as sitk
import os
import numpy as np
from tqdm import trange


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r''
    save_path = r''
    img_list = get_listdir(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        sitk_img = sitk.ReadImage(img_list[i])
        img_arr = sitk.GetArrayFromImage(sitk_img)
        f = np.fft.fftn(img_arr)
        fshift = np.fft.fftshift(f)
        fimg = np.log(np.abs(fshift))

        new_img = sitk.GetImageFromArray(fimg)
        new_img.CopyInformation(sitk_img)
        _, fullflname = os.path.split(img_list[i])
        sitk.WriteImage(new_img, os.path.join(save_path, fullflname))
