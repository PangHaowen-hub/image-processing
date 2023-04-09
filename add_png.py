import SimpleITK as sitk
import os
from PIL import Image
import numpy as np
from tqdm import trange
import cv2
import matplotlib.pyplot as plt

def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    png_path = r'I:\paper\8-vessel_map\grad_cam\COPD\_1'
    img_list = get_listdir(png_path)
    img_list.sort()
    sum_img = np.zeros((1440, 1920))
    for i in trange(len(img_list)):
        image = Image.open(img_list[i])
        img = np.array(image)
        sum_img += np.mean(img, axis=2)
    sum_img = sum_img / len(img_list)
    temp = sum_img.astype(np.uint8)
    temp[temp == 255] = 0
    temp = temp[45:1395, 285:1635]
    plt.axis('off')
    plt.imshow(temp)
    plt.savefig(r"I:\paper\8-vessel_map\grad_cam\COPD\1.png")
    print(sum_img)
