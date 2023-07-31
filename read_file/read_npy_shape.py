import numpy as np
import os
from tqdm import trange

def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.npy':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'F:\my_code\chenshannan\pytorch-CycleGAN-and-pix2pix-master\datasets\DWI2FLARI\trainA'
    img = get_listdir(img_path)
    img.sort()
    shape = []

    for i in trange(len(img)):
        data = np.load(img[i])
        shape.append(data.shape[1])

    shape.sort()
    print(shape)
