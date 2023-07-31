import os
import SimpleITK as sitk
import tqdm

count = 0
filepath = r'G:\Lobectomy\dalian\RUL\after\mask\temp'
filenames = os.listdir(filepath)  # 读取nii文件夹
print(filenames)

for f in tqdm.tqdm(filenames):
    if f[-1] == 'i':
        # 开始读取nii文件
        img_path = os.path.join(filepath, f)
        img = sitk.ReadImage(img_path)
        path = img_path + '.gz'
        sitk.WriteImage(img, path)