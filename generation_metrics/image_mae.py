import SimpleITK
import tqdm
from evalutils.io import SimpleITKLoader
import numpy as np
from typing import Optional
from skimage.metrics import peak_signal_noise_ratio, structural_similarity
import os
import seaborn as sns
import matplotlib.pyplot as plt

class ImageMetrics():
    def __init__(self):
        self.dynamic_range = 3000 - -1024

    def score_patient(self, ground_truth_path, predicted_path):
        loader = SimpleITKLoader()
        gt = loader.load_image(ground_truth_path)
        pred = loader.load_image(predicted_path)

        caster = SimpleITK.CastImageFilter()
        caster.SetOutputPixelType(SimpleITK.sitkFloat32)
        caster.SetNumberOfThreads(1)

        gt = caster.Execute(gt)
        pred = caster.Execute(pred)

        # Get numpy array from SITK Image
        gt_array = SimpleITK.GetArrayFromImage(gt)
        pred_array = SimpleITK.GetArrayFromImage(pred)

        mask_array = np.ones(gt_array.shape, dtype=gt_array.dtype)

        # Calculate image metrics
        mae_value = self.mae(gt_array, pred_array, mask_array)

        return {'mae': mae_value}

    def mae(self, gt: np.ndarray, pred: np.ndarray, mask: Optional[np.ndarray] = None) -> float:
        if mask is None:
            mask = np.ones(gt.shape)
        else:
            # binarize mask
            mask = np.where(mask > 0, 1., 0.)

        mae_value = np.sum(np.abs(gt * mask - pred * mask)) / mask.sum()
        return float(mae_value)


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    metrics = ImageMetrics()
    ground_truth_path = r"C:\Users\40702\Desktop\temp\T1_10_dose.nii.gz"
    predicted_path = r"C:\Users\40702\Desktop\temp\weighted_sum"
    predicted_list = get_listdir(predicted_path)

    predicted_list.sort()
    mae = []

    for i in tqdm.trange(len(predicted_list)):
        metrics_dict = metrics.score_patient(ground_truth_path, predicted_list[i])
        mae.append(metrics_dict['mae'])

    sns.lineplot(data=mae)
    plt.savefig('loss.png')  # 保存图片
    plt.show()
    # print(mae)
