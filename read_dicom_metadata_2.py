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
        if os.path.splitext(file)[1] == '.ima' or os.path.splitext(file)[1] == '.dcm':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_all_file(path):
    dcm_path = None
    try:
        filelist = os.listdir(path)[0]
        allfilelist = os.listdir(os.path.join(path, filelist))
        dcm_path = os.path.join(path, filelist, allfilelist[0])
        return dcm_path
    except:
        return dcm_path


def loadFileInformation(filename):
    information = {}
    try:
        ds = pydicom.read_file(filename)
        information['AcquisitionDate'] = ds.AcquisitionDate
        information['PatientName'] = ds.PatientName
        information['PatientSex'] = ds.PatientSex
        information['PatientAge'] = ds.PatientAge
        information['KVP'] = ds.KVP
        information['PixelSpacing'] = ds.PixelSpacing
        information['SliceThickness'] = ds.SliceThickness
        information['XRayTubeCurrent'] = ds.XRayTubeCurrent
        information['Manufacturer'] = ds.Manufacturer
        return information
    except:
        information['AcquisitionDate'] = 0
        information['PatientName'] = 0
        information['PatientSex'] = 0
        information['PatientAge'] = 0
        information['KVP'] = 0
        information['PixelSpacing'] = 0
        information['SliceThickness'] = 0
        information['XRayTubeCurrent'] = 0
        information['Manufacturer'] = 0
        return information


if __name__ == '__main__':
    allpath = []
    img_path = r'G:\gz_data\double_gas\image_486'
    img_list = get_listdir(img_path)
    img_list.sort()
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
    worksheet = workbook.add_sheet('info')  # 创建一个worksheet
    for i in tqdm.trange(len(img_list)):
        img_name = get_all_file(img_list[i])
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
        worksheet.write(i, 9, label=str(information['AcquisitionDate']))

    workbook.save(r'G:\gz_data\double_gas\data_486_2.xls')  # 保存
