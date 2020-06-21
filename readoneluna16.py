# 读取某一个mhd文件中数据并保存为png格式

import SimpleITK as sitk
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filename = './1.3.6.1.4.1.14519.5.2.1.6279.6001.128023902651233986592378348912.mhd'
    itkimage = sitk.ReadImage(filename)  # 读取.mhd文件
    numpyImage = sitk.GetArrayFromImage(itkimage)  # 获取数据，自动从同名的.raw文件读取
    print(numpyImage.shape)

    for i in range(0, numpyImage.shape[0]):
        data = numpyImage[i]
        plt.imsave(str(i) + '.png', data, format='png', cmap='gray')
