import SimpleITK as sitk
import os
from PIL import Image
import numpy as np
from tqdm import trange


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    png_path = r'C:\Users\User\Desktop\001.nii.jpg'
    save_path = r'C:\Users\User\Desktop'

    image = Image.open(png_path)
    image0 = np.array(image)
    for i in range(4):
        for j in range(4):
            x = i * 128
            y = j * 128
            out = image0[x:x + 128, y:y + 128]
            out = Image.fromarray(out)
            out.save(os.path.join(save_path, str(i) + str(j) + '.jpg'))
