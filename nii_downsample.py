import SimpleITK as sitk
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def down(img_path, save_path):
    scale = 2  # TODO:采样倍数
    sitk_img = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    new_arr = img_arr[::scale, ::scale, ::scale]
    new_img = sitk.GetImageFromArray(new_arr)
    new_img.SetDirection(sitk_img.GetDirection())
    new_img.SetOrigin(sitk_img.GetOrigin())
    Spacing = tuple([j * scale for j in sitk_img.GetSpacing()])
    new_img.SetSpacing(Spacing)
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    nii_path = r'C:\Users\40702\Desktop\temp'
    save_path = r'C:\Users\40702\Desktop\temp_down'
    l_nii = get_listdir(nii_path)
    l_nii.sort()
    for i in range(len(l_nii)):
        down(l_nii[i], save_path)
