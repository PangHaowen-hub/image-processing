import SimpleITK as sitk
import os
import numpy as np
from tqdm import trange
from matplotlib import pyplot as plt


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
        img = img_arr[50, :, :]
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        fimg = np.log(np.abs(fshift))

        plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Fourier')
        plt.axis('off')
        plt.subplot(122), plt.imshow(fimg, 'gray'), plt.title('Fourier Fourier')
        plt.axis('off')
        plt.show()
