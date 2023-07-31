import numpy as np
import SimpleITK as sitk


def raw2nii(path, shape, spacing):
    img_data = np.fromfile(path, dtype='int16')
    data_new_shape = img_data.reshape(shape)
    image = sitk.GetImageFromArray(data_new_shape)
    direction = (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, -1.0)
    image.SetDirection(direction)
    image.SetSpacing(spacing)
    sitk.WriteImage(image, path[-15:-4] + '.nii.gz')


if __name__ == '__main__':
    path = 'F:/DIR-lab/copd1/copd1/copd1_eBHCT.img'
    shape = [121, 512, 512]
    spacing = [0.625, 0.625, 2.5]
    raw2nii(path, shape, spacing)
