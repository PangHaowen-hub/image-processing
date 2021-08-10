import cv2
import os


def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


path = r'E:\CAS\gtihub_code\AttaNet_1280_720\data\satellite_test\images\val_temp'
img_list = get_listdir(path, '.png')
for i in img_list:
    img = cv2.imread(i)
    _, fullflname = os.path.split(i)
    ret = cv2.copyMakeBorder(img, 2, 2, 800, 800, cv2.BORDER_CONSTANT, value=(70,70,70))
    OpenCV_test = cv2.resize(ret, (1280, 720))
    cv2.imwrite(os.path.join('./data/satellite_test/images/val', fullflname)[:-4] + '.jpg', OpenCV_test)
