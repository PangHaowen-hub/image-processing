import SimpleITK as sitk
import os


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(img, img_save_path):
    sitk_img = sitk.ReadImage(img)
    img_arr = sitk.GetArrayFromImage(sitk_img)
    MIN_BOUND = -1000.0
    MAX_BOUND = 400.0
    img_arr[img_arr > MAX_BOUND] = MAX_BOUND
    img_arr[img_arr < MIN_BOUND] = MIN_BOUND
    img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)

    new_img = sitk.GetImageFromArray(img_arr)
    new_img.SetSpacing(sitk_img.GetSpacing())
    new_img.SetOrigin(sitk_img.GetOrigin())
    new_img.SetDirection(sitk_img.GetDirection())

    _, fullflname = os.path.split(img)
    sitk.WriteImage(new_img, os.path.join(img_save_path, fullflname))


if __name__ == '__main__':
    img_path = r'D:\github_code\VoxelMorph-torch-master\Dataset\Lobe_256_norm'
    save_path = r'D:\github_code\VoxelMorph-torch-master\Dataset\Lobe_256_norm'

    img_list = get_listdir(img_path)
    img_list.sort()
    for i in range(len(img_list)):
        add_label(img_list[i], save_path)
