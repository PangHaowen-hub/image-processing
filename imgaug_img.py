import imageio
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.segmaps import SegmentationMapsOnImage
from PIL import Image
import os

ia.seed(1)


def get_listdir_jpg(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.jpg':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def aug(img):
    image = Image.open(img)
    image = np.array(image)

    seq = iaa.Sequential([
        iaa.AdditiveGaussianNoise(scale=0.2 * 255),
    ], random_order=True)

    _, fullflname = os.path.split(img)
    images_aug_i = seq(image=image)
    imageio.imwrite('E:/CAS/gtihub_code/AttaNet_1280_720/data/satellite_1280_720_aug/images/train/' + fullflname,
                    images_aug_i)


if __name__ == '__main__':
    img_path = r'E:\CAS\gtihub_code\AttaNet_1280_720\data\satellite_1280_720_aug\images\train'
    img_list = get_listdir_jpg(img_path)
    img_list.sort()
    for i in range(len(img_list)):
        aug(img_list[i])
