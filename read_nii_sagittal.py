import SimpleITK as sitk
import os
import numpy as np
from PIL import Image
import cv2

img_path = r'C:\Users\User\Desktop\025.nii.gz'

sitk_img = sitk.ReadImage(img_path)
img_arr = sitk.GetArrayFromImage(sitk_img)
spacing = sitk_img.GetSpacing()

MIN_BOUND = -1000.0
MAX_BOUND = 400.0
img_arr[img_arr > MAX_BOUND] = MAX_BOUND
img_arr[img_arr < MIN_BOUND] = MIN_BOUND
img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND) * 255
temp = img_arr[:, :, 209].astype(np.uint8)

temp = np.flip(temp, axis=0)
temp = cv2.resize(temp, (int(741 * spacing[2]), int(512 * spacing[0])), interpolation=cv2.INTER_LINEAR)

img_pil = Image.fromarray(temp)
img_pil.save(r'C:\Users\User\Desktop\temp.png')
