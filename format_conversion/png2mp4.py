import os
import cv2
from PIL import Image


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


fps = 2
size = (1280, 720)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

path = r'.\test_true_norm'
video_path = './test_true_norm.mp4'
img_list = get_listdir(path)
img_list.sort()
vw = cv2.VideoWriter(video_path, fourcc, fps, size)
for i in img_list:
    frame = cv2.imread(i)
    vw.write(frame)
