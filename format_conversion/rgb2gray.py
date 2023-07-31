from PIL import Image
import os


def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


path = r'F:\卫星测试数据\focal-length75mm-left-15-up-30-interval0.5m'
save_path = ''
img_list = get_listdir(path, '.png')
for i in img_list:
    _, img_name = os.path.split(i)
    I = Image.open(i)
    I.show()
    L = I.convert('L')
    L.save(os.path.join(save_path, img_name))
