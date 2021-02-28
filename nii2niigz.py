import os
import SimpleITK as sitk

count = 0
filepath = r'F:\lobe\lobe_data_lobe\RU_final\before\mask'
filenames = os.listdir(filepath)  # 读取nii文件夹
print(filenames)

for f in filenames:
    if f[-1] == 'i':
        # 开始读取nii文件
        img_path = os.path.join(filepath, f)
        img = sitk.ReadImage(img_path)
        path = img_path + '.gz'
        sitk.WriteImage(img, path)