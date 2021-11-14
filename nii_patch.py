import torch
import argparse
from torch.utils.data import DataLoader
import numpy as np
import os
import tqdm
import torchio
from torchio.transforms import ZNormalization, CropOrPad, Compose, Resample, Resize
import SimpleITK as sitk

import torch.utils.data as data
import os
from torchio.data import UniformSampler
from torchio.transforms import ZNormalization, CropOrPad, Compose, Resample, Resize
import torchio


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


class test_dataset(data.Dataset):
    def __init__(self, imgs_path):
        self.img_list = get_listdir(imgs_path)
        self.img_list.sort()
        self.subjects = []
        for image_path in self.img_list:
            subject = torchio.Subject(
                source=torchio.ScalarImage(image_path)
            )
            self.subjects.append(subject)
        self.transforms = self.transform()

        self.test_set = torchio.SubjectsDataset(self.subjects, transform=self.transforms)

    def transform(self):
        test_transform = Compose([
            ZNormalization(),
        ])
        return test_transform

    def get_shape(self, i):
        return self.subjects[i].shape


if __name__ == '__main__':
    batch_size = 1
    source_test_dir = r'G:\CT2CECT\registration\moving_a_resample_norm'
    save_path = r'G:\CT2CECT\registration\moving_a_resample_norm_patch'
    dataset = test_dataset(source_test_dir)
    patch_overlap = 128, 128, 128
    patch_size = 256

    for i, subj in enumerate(dataset.test_set):
        grid_sampler = torchio.inference.GridSampler(subj, patch_size, patch_overlap)
        patch_loader = torch.utils.data.DataLoader(grid_sampler, batch_size)
        aggregator = torchio.inference.GridAggregator(grid_sampler, 'average')

        for j, patches_batch in enumerate(patch_loader):
            input_tensor = patches_batch['source'][torchio.DATA].float()
            locations = patches_batch[torchio.LOCATION]  # patch的位置信息
            _, fullflname = os.path.split(subj['source']['path'])
            affine = subj['source']['affine']
            output_arr = np.squeeze(input_tensor.numpy(), 0)
            output_image = torchio.ScalarImage(tensor=output_arr, affine=affine)
            output_image.save(
                os.path.join(save_path, os.path.join(save_path, fullflname[:-7] + str(j).rjust(2, '0') + '.nii.gz')))
