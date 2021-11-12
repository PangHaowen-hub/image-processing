import SimpleITK as sitk
from tqdm import trange
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def difference(img1_path, img2_path, save_path):
    img1 = sitk.ReadImage(img1_path)
    img1_arr = sitk.GetArrayFromImage(img1)
    img2 = sitk.ReadImage(img2_path)
    img2_arr = sitk.GetArrayFromImage(img2)

    diff_img_arr = img1_arr - img2_arr

    diff_img = sitk.GetImageFromArray(diff_img_arr)
    diff_img.SetDirection(img1.GetDirection())
    diff_img.SetOrigin(img1.GetOrigin())
    diff_img.SetSpacing(img1.GetSpacing())
    _, fullflname = os.path.split(img1_path)
    sitk.WriteImage(diff_img, os.path.join(save_path, fullflname))


if __name__ == '__main__':
    img1_path = r'G:\lobe_registration\LL\after\LU_Lobe_resample_pad_norm'
    img2_path = r'G:\lobe_registration\LL\registrated\warped'
    save_path = r'G:\lobe_registration\LL\difference'
    img1 = get_listdir(img1_path)
    img1.sort()
    img2 = get_listdir(img2_path)
    img2.sort()
    for i in trange(len(img1)):
        difference(img1[i], img2[i], save_path)
