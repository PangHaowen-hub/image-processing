import cv2
import os


def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


path = r'F:\github_code\denoising-diffusion-pytorch-main\data\png'
img_list = get_listdir(path, '.png')
desired_size = 1280
for i in img_list:
    _, fullflname = os.path.split(i)
    im = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    im = cv2.resize(im, (128, 128))

    cv2.imwrite(os.path.join(r'F:\github_code\denoising-diffusion-pytorch-main\data\png', fullflname)[:-4] + '.png', im)
