import cv2
import os


def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


path = r'E:\CAS\github_code\AttaNet_1280\test_data'
img_list = get_listdir(path, '.png')
desired_size = 1280
for i in img_list:
    _, fullflname = os.path.split(i)
    im = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    old_size = im.shape[:2]  # old_size is in (height, width) format

    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])

    # new_size should be in (width, height) format

    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)
    cv2.imwrite(os.path.join(r'E:\CAS\github_code\AttaNet_1280\test_data_2', fullflname)[:-4] + '.jpg', new_im)
