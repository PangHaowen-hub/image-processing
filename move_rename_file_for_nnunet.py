import os
import shutil
import tqdm


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    img_path = r'/data3/haowenpang/my_code/MRI-Synthesis-Foundation-Model/data/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData'

    img_list = os.listdir(img_path)
    img_list.sort()

    image_save_path = r'/data8/haowenpang/nnUNet_raw/Dataset002_t1t2flair1/imagesTr'
    label_save_path = r'/data8/haowenpang/nnUNet_raw/Dataset002_t1t2flair1/labelsTr'
    os.makedirs(image_save_path, exist_ok=True)
    os.makedirs(label_save_path, exist_ok=True)
    for i in tqdm.tqdm(img_list):
        for j in os.listdir(os.path.join(img_path, i)):
            name = os.path.join(img_path, i, j)

            if '-t1n' in j:
                shutil.copy(name, os.path.join(image_save_path, j.replace('-t1n', '_0000')))
            elif '-t2w' in j:
                shutil.copy(name, os.path.join(image_save_path, j.replace('-t2w', '_0001')))
            elif '-t2f' in j:
                shutil.copy(name, os.path.join(image_save_path, j.replace('-t2f', '_0002')))
            # elif '-seg' in j:
            #     shutil.copy(name, os.path.join(label_save_path, j.replace('-seg', '')))
