import os
import h5py
import numpy as np
import SimpleITK as sitk
from tqdm import trange


def create_info(matrix, voxel_size, read_points, read_gap, spokes_hi, spokes_lo, lo_scale,
                channels, volumes, tr=0, origin=[0, 0, 0], direction=None):
    """
    Creates a numpy structured array for riesling h5 files.

    Inputs:
        - matrix: Matrix size (x,y,z)
        - voxel_size: Voxel size in mm (x,y,z)
        - read_points: Number of readout points along the spoke
        - read_gap: Deadtime gap
        - spokes_hi: Number of highres spokes
        - spokes_lo: Number of lowres spokes
        - lo_scale: Scale factor of the low res spokes
        - channels: Number of receive channels
        - volumes: Number of volumes
        - tr: Repetition time (Default=0)
        - origin: Origin of image (x,y,z) (Default: 0,0,0)
        - direction: Orientation matrix (Default: eye)

    Return: D (structured numpy array)
    """

    if not direction:
        direction = np.eye(3)

    D = np.dtype({'names': [
        'matrix',
        'voxel_size',
        'read_points',
        'read_gap',
        'spokes_hi',
        'spokes_lo',
        'lo_scale',
        'channels',
        'volumes',
        'tr',
        'origin',
        'direction'],
        'formats': [
            ('<i8', (3,)),
            ('<f4', (3,)),
            '<i8',
            '<i8',
            '<i8',
            '<i8',
            '<f4',
            '<i8',
            '<i8',
            '<f4',
            ('<f4', (3,)),
            ('<f4', (9,))]
    })

    info = np.array([(matrix, voxel_size, read_points, read_gap, spokes_hi, spokes_lo, lo_scale,
                      channels, volumes, tr, origin, direction)], dtype=D)

    return info


def nii2h5(img_name, save_path):
    """
    Converts a nifti file to riesling format .h5 image file
    """
    img = sitk.ReadImage(img_name)
    origin = img.GetOrigin()
    spacing = img.GetSpacing()
    direction = img.GetDirection()
    img_data = sitk.GetArrayFromImage(img)

    info = create_info(matrix=[0, 0, 0],
                       voxel_size=list(spacing),
                       read_points=0, read_gap=0, spokes_hi=0, spokes_lo=0, lo_scale=0,
                       channels=1, volumes=1, origin=list(origin), direction=list(direction))

    _, fullflname = os.path.split(img_name)
    output_name = os.path.join(save_path, fullflname[:-7] + '.h5')

    h5 = h5py.File(output_name, 'w')
    h5.create_dataset('image', data=img_data[np.newaxis, ...])
    h5.create_dataset('info', data=info)
    h5.close()


def h52nii(img_name, save_path):
    """
    Converts riesling image .h5 file to nifti.
    """
    f = h5py.File(img_name, 'r')
    info = f['info'][:]

    data = f['image'][0, ...]
    f.close()

    voxel_size = np.array(info['voxel_size'][0], dtype=float)
    origin = np.array(info['origin'][0], dtype=float)
    direction = np.array(info['direction'][0], dtype=float)

    img = sitk.GetImageFromArray(data)

    img.SetOrigin(origin)
    img.SetSpacing(voxel_size)
    img.SetDirection(direction)

    _, fullflname = os.path.split(img_name)
    output_name = os.path.join(save_path, fullflname[:-3] + '.nii.gz')

    writer = sitk.ImageFileWriter()
    writer.SetFileName(output_name)
    writer.Execute(img)


def get_nii_list(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def get_h5_list(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.h5':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    # img_path = r'H:\PRM\59_cases_nii\segmentation\PRM_rename_I'
    # save_path = r'F:\github_code\pytorch-3dunet-master\data\PRM_h5'
    # img_list = get_nii_list(img_path)
    # img_list.sort()
    # for i in trange(len(img_list)):
    #     nii2h5(img_list[i], save_path)

    img_path = r'F:\github_code\pytorch-3dunet-master\data\temp'
    save_path = r'F:\github_code\pytorch-3dunet-master\data'
    img_list = get_h5_list(img_path)
    img_list.sort()
    for i in trange(len(img_list)):
        h52nii(img_list[i], save_path)
