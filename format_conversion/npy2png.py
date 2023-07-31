import numpy as np
from PIL import Image

data = np.load(r'F:\my_code\pix2pix-ct2cect\data\CT2CECT_npy\train\A\ct_000_0000.nii.gz00020.npy')
MIN_BOUND = -1000.0
MAX_BOUND = 400.0
data[data > MAX_BOUND] = MAX_BOUND
data[data < MIN_BOUND] = MIN_BOUND
img_arr = (data - MIN_BOUND) / (MAX_BOUND - MIN_BOUND) * 255
temp = img_arr.astype(np.uint8)
img_pil = Image.fromarray(temp)
img_pil.save('test.png')