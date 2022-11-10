import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'G:\parse2022\image'
    save_path = r'G:\parse2022\image.txt'
    path_list = get_listdir(img_path)
    path_list.sort()
    for file_name in path_list:
        # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
        with open(save_path, "a") as file:
            file.write(file_name + "\n")
            print(file_name)
        file.close()
