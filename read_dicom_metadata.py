import pydicom
import os
import tqdm
import collections
import xlwt


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        tmp_list.append(file_path)
    return tmp_list

def get_listdir_dcm(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.dcm':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list

def loadFileInformation(filename):
    information = {}
    ds = pydicom.read_file(filename)
    information['PatientName'] = ds.PatientName
    information['PatientSex'] = ds.PatientSex
    information['PatientAge'] = ds.PatientAge
    information['KVP'] = ds.KVP
    information['PixelSpacing'] = ds.PixelSpacing
    information['SliceThickness'] = ds.SliceThickness
    information['XRayTubeCurrent'] = ds.XRayTubeCurrent
    information['Manufacturer'] = ds.Manufacturer
    return information


if __name__ == '__main__':
    img_path = r'G:\Lobectomy\shengjing\RLL'
    img_list = get_listdir(img_path)
    img_list.sort()
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
    worksheet = workbook.add_sheet('info')  # 创建一个worksheet
    for i in tqdm.trange(len(img_list)):
        img_name = get_listdir_dcm(img_list[i])[0]
        information = loadFileInformation(img_name)
        worksheet.write(i, 0, label=img_list[i])
        worksheet.write(i, 1, label=str(information['PatientName']))
        worksheet.write(i, 2, label=str(information['PatientSex']))
        worksheet.write(i, 3, label=str(information['PatientAge']))
        worksheet.write(i, 4, label=str(information['KVP']))
        worksheet.write(i, 5, label=str(information['PixelSpacing']))
        worksheet.write(i, 6, label=str(information['SliceThickness']))
        worksheet.write(i, 7, label=str(information['XRayTubeCurrent']))
        worksheet.write(i, 8, label=str(information['Manufacturer']))
    workbook.save(r'G:\Lobectomy\shengjing\RLL_info.xls')  # 保存
