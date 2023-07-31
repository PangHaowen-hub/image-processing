import os
import pydicom
import numpy
import SimpleITK

# 路径和列表声明
PathDicom = r"C:\Users\Administrator\Desktop\4DCT-Dicom"  # 与python文件同一个目录下的文件夹,存储dicom文件
SaveRawDicom = "./"  # 与python文件同一个目录下的文件夹,用来存储mhd文件和raw文件
lstFilesDCM = []

# 将PathDicom文件夹下的dicom文件地址读取到lstFilesDCM中
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # 判断文件是否为dicom文件
            # print(filename)
            lstFilesDCM.append(os.path.join(dirName, filename))  # 加入到列表中

# 第一步：将第一张图片作为参考图片，并认为所有图片具有相同维度
RefDs = pydicom.read_file(lstFilesDCM[0])  # 读取第一张dicom图片

# 第二步：得到dicom图片所组成3D图片的维度
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), 141, 10)  # ConstPixelDims是一个元组

# 第三步：得到x方向和y方向的Spacing并得到z方向的层厚
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness), 1)

# 第四步：得到图像的原点、方向
# Origin = RefDs.ImagePositionPatient
direction = (1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0)


# 根据维度创建一个numpy的三维数组，并将元素类型设为：pixel_array.dtype
ArrayDicom = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)  # array is a numpy array

# 第五步:遍历所有的dicom文件，读取图像数据，存放在numpy数组中
for i in range(len(lstFilesDCM)):
    ds = pydicom.read_file(lstFilesDCM[i])
    ArrayDicom[:, :, i % 141, i // 141] = ds.pixel_array


# 第六步：对numpy数组进行转置，即把坐标轴（x,y,z）变换为（z,y,x）,这样是dicom存储文件的格式，即第一个维度为z轴便于图片堆叠
ArrayDicom = numpy.transpose(ArrayDicom, (3, 2, 0, 1))

# 第七步：将现在的numpy数组通过SimpleITK转化为mhd和raw文件
sitk_img = SimpleITK.GetImageFromArray(ArrayDicom, isVector=False)
sitk_img.SetSpacing(ConstPixelSpacing)
sitk_img.SetDirection(direction)
# sitk_img.SetOrigin(Origin)
SimpleITK.WriteImage(sitk_img, os.path.join(SaveRawDicom, "sample" + ".mhd"))
