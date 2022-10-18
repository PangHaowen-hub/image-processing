from PIL import Image
import os
import tqdm

def get_listdir(path, format):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == format:
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


path = r'F:\my_code\NCCT2CECT\ResViT\datasets\NCCT2CECT\valB'
save_path = r'F:\my_code\NCCT2CECT\ResViT\datasets\NCCT2CECT\valB'
img_list = get_listdir(path, '.png')
img_list.sort()

for i in tqdm.tqdm(img_list):
    _, img_name = os.path.split(i)
    I = Image.open(i)
    # I.show()
    L = I.convert('RGB')
    L.save(os.path.join(save_path, img_name))
