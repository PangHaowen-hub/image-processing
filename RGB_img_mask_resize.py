import os
import cv2
import numpy as np
from PIL import Image


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


def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def test(img, Weight_out, Height_out):
    # 获取图像的大小
    Height_in, Weight_in = img.shape
    # 创建输出图像
    outimg = np.zeros((Height_out, Weight_out), dtype=np.uint8)

    for x in range(Height_out - 1):
        for y in range(Weight_out - 1):
            # 计算输出图像坐标（i,j）坐标使用输入图像中的哪个坐标来填充
            x_out = int(x * (Height_in / Height_out))
            y_out = int(y * (Weight_in / Weight_out))
            # 插值
            outimg[x, y] = img[x_out, y_out]
    return outimg


# # 原图
# path = r'E:\CAS\gtihub_code\AttaNet_1280_720\data\satellite\images\test'
# img_list = get_listdir(path, '.jpg')
# for i in img_list:
#     img = cv2.imread(i)
#     OpenCV_test = cv2.resize(img, (1280, 720))
#     cv2.imwrite(i[-10:], OpenCV_test)




# # mask
# color_map = get_color_map_list(256)
# path = r'E:\CAS\gtihub_code\AttaNet_1280_720\data\satellite\labels\val'
# img_list = get_listdir(path, '.png')
# for i in img_list:
#     img = cv2.imread(i)
#     img_0 = img[:, :, 0]  # 第三
#     img_1 = img[:, :, 1]  # 第二
#     img_2 = img[:, :, 2]  # 第一
#     img_0[img_0 == 128] = 3
#     img_0[img_2 == 128] = 0
#     img_0[img_1 == 128] = 1
#     temp = img_1.astype(np.int) + img_2.astype(np.int)
#     img_0[temp == 256] = 2
#     # img_0[img_1 == 128 and img_2 == 128] = 2
#     OpenCV_test = img_0
#     OpenCV_test = test(OpenCV_test, 1280, 720)
#     lbl_pil = Image.fromarray(OpenCV_test.astype(np.uint8), mode='P')
#     lbl_pil.putpalette(color_map)
#     lbl_pil.save(i[-10:])
