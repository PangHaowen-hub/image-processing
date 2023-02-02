import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.png':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


save_path = r"G:\gz_data\double_gas\image_486.txt"
dir_path = r"G:\gz_data\double_gas\image_486"  # 文件路径
path_list = os.listdir(dir_path)
# path_list = get_listdir(dir_path)  # 遍历整个文件夹下的文件name并返回一个列表
path_list.sort()

for file_name in path_list:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open(save_path, "a") as file:
        # file_name = file_name + ', 0'
        file.write(file_name + "\n")
        print(file_name)
    file.close()
