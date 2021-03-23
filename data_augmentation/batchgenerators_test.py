import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from batchgenerators.dataloading.data_loader import SlimDataLoaderBase
from batchgenerators.transforms.spatial_transforms import SpatialTransform  # 旋转缩放
from batchgenerators.transforms.noise_transforms import GaussianNoiseTransform, GaussianBlurTransform  # 高斯噪声、模糊
from batchgenerators.transforms.color_transforms import BrightnessTransform  # 亮度
from batchgenerators.transforms.color_transforms import ContrastAugmentationTransform  # 对比度
from batchgenerators.transforms.resample_transforms import SimulateLowResolutionTransform  # 低分辨率模拟
from batchgenerators.transforms import GammaTransform  # 伽马增强
from batchgenerators.transforms.spatial_transforms import MirrorTransform  # 镜像

from batchgenerators.transforms.abstract_transforms import Compose

from batchgenerators.dataloading.multi_threaded_augmenter import MultiThreadedAugmenter
import cv2

matplotlib.use('Agg')


class DataLoader(SlimDataLoaderBase):
    def __init__(self, data, BATCH_SIZE=2, number_of_threads_in_multithreaded=None):
        super(DataLoader, self).__init__(data, BATCH_SIZE, number_of_threads_in_multithreaded)
        # data is now stored in self._data.

    def generate_train_batch(self):
        # usually you would now select random instances of your data. We only have one therefore we skip this
        img = self._data
        # The camera image has only one channel. Our batch layout must be (b, c, x, y). Let's fix that
        img = np.tile(img[None, None], (self.batch_size, 1, 1, 1))
        # now construct the dictionary and return it. np.float32 cast because most networks take float
        return {'data': img.astype(np.float32), 'some_other_key': 'some other value'}


def plot_batch(batch):
    batch_size = batch['data'].shape[0]
    for i in range(batch_size):
        temp = batch['data'][i, 0]
        cv2.imwrite('./img/' + str(i) + '.png', temp)


img = plt.imread("img.jpg")
batchgen = DataLoader(img, 32, None)

my_transforms = []
spatial_transform = SpatialTransform(img.shape, np.array(img.shape) // 2,
                                     do_elastic_deform=False,
                                     do_rotation=True, angle_z=(0, 2 * np.pi),  # 旋转
                                     do_scale=True, scale=(0.3, 3.),  # 缩放
                                     border_mode_data='constant', border_cval_data=0, order_data=1,
                                     random_crop=False)
my_transforms.append(spatial_transform)
GaussianNoise = GaussianNoiseTransform()  # 高斯噪声
my_transforms.append(GaussianNoise)
GaussianBlur = GaussianBlurTransform()  # 高斯模糊
my_transforms.append(GaussianBlur)
Brightness = BrightnessTransform(0, 0.2)  # 亮度
my_transforms.append(Brightness)
brightness_transform = ContrastAugmentationTransform((0.3, 3.), preserve_range=True)  # 对比度
my_transforms.append(brightness_transform)
SimulateLowResolution = SimulateLowResolutionTransform()  # 低分辨率
my_transforms.append(SimulateLowResolution)
Gamma = GammaTransform()  # 伽马增强
my_transforms.append(Gamma)
mirror_transform = MirrorTransform(axes=(0, 1))  # 镜像
my_transforms.append(mirror_transform)
all_transforms = Compose(my_transforms)
multithreaded_generator = MultiThreadedAugmenter(batchgen, all_transforms, 1, 2)

t = multithreaded_generator.next()
plot_batch(t)
