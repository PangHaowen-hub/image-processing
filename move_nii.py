import os
import shutil
import tqdm


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'G:\parse2022\train'
    image_save_path = r'G:\parse2022\image'
    label_save_path = r'G:\parse2022\label'

    img_list = os.listdir(img_path)
    img_list.sort()
    for i in tqdm.tqdm(img_list):
        path_image = os.path.join(img_path, i, 'image')
        image_path = get_listdir(path_image)[0]
        _, fullflname = os.path.split(image_path)
        shutil.copy(image_path, os.path.join(image_save_path, fullflname))

        path_label = os.path.join(img_path, i, 'label')
        label_path = get_listdir(path_label)[0]
        _, fullflname = os.path.split(label_path)
        shutil.copy(label_path, os.path.join(label_save_path, fullflname))
