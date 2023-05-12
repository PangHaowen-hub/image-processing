import pickle
import os
import collections
from sklearn.model_selection import train_test_split


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            tmp_list.append(file[:-12])
    return tmp_list


if __name__ == '__main__':
    img_path = '/disk1/panghaowen/CoTr/nnUNet_raw_data_base/nnUNet_raw_data/Task126_SNCCTvesselD2/imagesTr'
    save_path = r'/disk1/panghaowen/CoTr/data/splits_final_126.pkl'
    path_list = get_listdir(img_path)
    path_list.sort()
    train_list, val_list = train_test_split(path_list, train_size=0.9, shuffle=True)
    dic = collections.OrderedDict()
    dic['train'] = train_list
    dic['val'] = val_list
    pickle_file = open(save_path, 'wb')
    pickle.dump([dic], pickle_file)
    pickle_file.close()
