from typing import Tuple
import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *


def get_identifiers_from_splitted_files(folder: str):
    uniques = np.unique([i[:-12] for i in subfiles(folder, suffix='.nii.gz', join=False)])
    return uniques


if __name__ == '__main__':

    output_file = r'/disk1/panghaowen/nnUNet-master/nnUNet_raw_data_base/nnUNet_raw_data/Task123_parse2022/dataset.json'
    imagesTr_dir = r'/disk1/panghaowen/nnUNet-master/nnUNet_raw_data_base/nnUNet_raw_data/Task123_parse2022/imagesTr'
    imagesTs_dir = r'/disk1/panghaowen/nnUNet-master/nnUNet_raw_data_base/nnUNet_raw_data/Task123_parse2022/imagesTs'
    modalities = ('CT',)
    labels = {0: 'background', 1: '1', }
    train_identifiers = get_identifiers_from_splitted_files(imagesTr_dir)

    if imagesTs_dir is not None:
        test_identifiers = get_identifiers_from_splitted_files(imagesTs_dir)
    else:
        test_identifiers = []

    json_dict = {}
    json_dict['name'] = 'parse2022'
    json_dict['description'] = 'segmentation'
    json_dict['tensorImageSize'] = "3D"
    json_dict['reference'] = 'NEU'
    json_dict['licence'] = "CC-BY-SA 4.0"
    json_dict['release'] = "1.0 1/5/2022",
    json_dict['modality'] = {str(i): modalities[i] for i in range(len(modalities))}
    json_dict['labels'] = {str(i): labels[i] for i in labels.keys()}

    json_dict['numTraining'] = len(train_identifiers)
    json_dict['numTest'] = len(test_identifiers)
    json_dict['training'] = [
        {'image': "./imagesTr/%s.nii.gz" % i, "label": "./labelsTr/%s.nii.gz" % i} for i
        in
        train_identifiers]
    json_dict['test'] = ["./imagesTs/%s.nii.gz" % i for i in test_identifiers]

    if not output_file.endswith("dataset.json"):
        print("WARNING: output file name is not dataset.json! This may be intentional or not. You decide. "
              "Proceeding anyways...")
    save_json(json_dict, os.path.join(output_file), sort_keys=True)
