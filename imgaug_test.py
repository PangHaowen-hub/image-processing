import imageio
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.segmaps import SegmentationMapsOnImage
from PIL import Image
import os

ia.seed(1)


def get_listdir_png(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_listdir_jpg(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.jpg':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_color_map_list(num_classes):
    num_classes += 1
    color_map = num_classes * [0, 0, 0]
    for i in range(0, num_classes):
        j = 0
        lab = i
        while lab:
            color_map[i * 3] |= (((lab >> 0) & 1) << (7 - j))
            color_map[i * 3 + 1] |= (((lab >> 1) & 1) << (7 - j))
            color_map[i * 3 + 2] |= (((lab >> 2) & 1) << (7 - j))
            j += 1
            lab >>= 3
    color_map = color_map[3:]
    return color_map


def aug(img, mask):
    image = Image.open(img)
    image = np.array(image)

    segmap = Image.open(mask)
    segmap = np.array(segmap)
    segmap = SegmentationMapsOnImage(segmap, shape=image.shape)

    seq = iaa.Sequential([
        iaa.AdditiveGaussianNoise(scale=0.1 * 255),
        iaa.Affine(rotate=(-90, 90)),
        iaa.CropAndPad(percent=(-0.25, 0.25))
    ], random_order=True)

    _, fullflname = os.path.split(img)
    fullflname = fullflname.split('.')[0]
    for j in range(3):
        images_aug_i, segmaps_aug_i = seq(image=image, segmentation_maps=segmap)
        imageio.imwrite('./data/satellite_true/aug/' + fullflname + '_' + str(j) + '.jpg', images_aug_i)

        temp = segmaps_aug_i.arr.squeeze().astype(np.uint8)
        lbl_pil = Image.fromarray(temp, mode='P')
        lbl_pil.putpalette(color_map)
        lbl_pil.save('./data/satellite_true/aug/' + fullflname + '_' + str(j) + '.png')


if __name__ == '__main__':
    color_map = get_color_map_list(256)
    img_path = r'.\data\satellite_true\images\train'
    mask_path = r'.\data\satellite_true\labels\train'
    img_list = get_listdir_jpg(img_path)
    mask_list = get_listdir_png(mask_path)
    img_list.sort()
    mask_list.sort()
    for i in range(len(img_list)):
        aug(img_list[i], mask_list[i])
