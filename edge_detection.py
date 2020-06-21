import cv2
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.png'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


root_img = 'E:/hbulndata/img'  # 原图文件夹路径
root_mask = 'E:/hbulndata/mask'  # mask文件夹路径
root_pred = 'E:/hbulndata/pred'  # 预测图文件夹路径
path_img = get_listdir(root_img)
path_mask = get_listdir(root_mask)
path_pred = get_listdir(root_pred)

for i in range(len(path_img)):

    mask = cv2.imread(path_mask[i])
    print(path_mask[i])
    pred = cv2.imread(path_pred[i])
    print(path_pred[i])

    # 二值化，canny检测
    binary_mask = cv2.Canny(mask, 30, 100)
    binary_pred = cv2.Canny(pred, 30, 100)

    # 寻找轮廓
    h_mask = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    h_pred = cv2.findContours(binary_pred, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # 提取轮廓
    contours_mask = h_mask[0]
    contours_pred = h_pred[0]

    img = cv2.imread(path_img[i])
    # 画出轮廓：contours是轮廓，-1表示全画，然后是颜色，厚度
    cv2.drawContours(img, contours_mask, -1, (0, 0, 255), 1)  # 红mask
    cv2.drawContours(img, contours_pred, -1, (0, 255, 0), 1)  # 绿预测

    cv2.imwrite('E:/hbulndata/result/' + str(i) + '.jpg', img)