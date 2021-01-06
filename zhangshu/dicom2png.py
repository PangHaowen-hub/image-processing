import SimpleITK as sitk
import numpy as np
import cv2
import os

count = 0

def dicom2png(path):
    global count
    filename = os.listdir(path)
    print(filename)
    for i in filename:
        document = os.path.join(path, i)
        ds_array = sitk.ReadImage(document)
        img_array = sitk.GetArrayFromImage(ds_array)

        shape = img_array.shape  # name.shape
        img_array = np.reshape(img_array, (shape[1], shape[2]))
        high = np.max(img_array)
        low = np.min(img_array)

        outputpath = "E:/pythondemo/lobeseg/data/preoperotive/test/dicom2png/"
        countname = str(count)
        countfullname = countname + '.png'
        output_png_path = os.path.join(outputpath, countfullname)
        print(output_png_path)

        lungwin = np.array([low * 1., high * 1.])
        newimg = (img_array - lungwin[0]) / (lungwin[1] - lungwin[0])
        newimg = (newimg * 255).astype('uint8')
        cv2.imwrite(output_png_path, newimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        count = count + 1


if __name__ == '__main__':
    path = "E:/pythondemo/lobeseg/data/preoperotive/test/dicom/"
    dirs = os.listdir(path)
    for dir in dirs:
        print(dir)
        dicom2png(path + dir)
