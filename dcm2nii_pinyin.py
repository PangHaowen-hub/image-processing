import os
import shutil
import tqdm
import pypinyin


def hp(word):  # 汉字改拼音
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


if __name__ == '__main__':
    path = r'G:\肺栓塞和钙化\肺栓塞'
    name_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        name_list.append(file_path)
    name_list.sort()
    for i in tqdm.trange(len(name_list)):
        i = name_list[i]
        name = i.split('\\')[-1]
        name = hp(name)
        os.mkdir(os.path.join(r"H:\CT2CECT\Pulmonary_embolism", name))
        num = os.listdir(i)
        i = os.path.join(i, num[0])
        dcm_list = os.listdir(i)
        dcm_list.sort()
        for j in dcm_list:
            dcm_path = os.path.join(i, j)
            shutil.copytree(dcm_path, os.path.join(r"H:\CT2CECT\Pulmonary_embolism", name, j))
