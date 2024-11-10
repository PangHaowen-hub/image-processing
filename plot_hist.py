import os
import matplotlib.pyplot as plt
import SimpleITK as sitk
import seaborn as sns
from PIL import Image
import pandas as pd
import numpy as np



if __name__ == '__main__':
    # path_before = r'C:\Users\40702\Desktop\after.nii.gz'
    path_before = r'C:\Users\40702\Desktop\before.nii'

    path_before_sitk_img = sitk.ReadImage(path_before)
    img_before = sitk.GetArrayFromImage(path_before_sitk_img)
    print(np.std(img_before))
    # img_before_arr = img_before.reshape(-1, 1).squeeze()
    #
    # data = {}
    # data['before'] = img_before_arr
    # frame = pd.DataFrame(data)
    #
    # sns.histplot(frame, element="poly", fill=False, legend=True)
    # plt.xlim(-0.4, 0.4)
    # # plt.ylim(0, 0.5)
    #
    # plt.yticks(fontproperties='Times New Roman', size=15, weight='bold')
    # plt.xticks(fontproperties='Times New Roman', size=15, weight='bold')
    # plt.ylabel("Count", fontsize=15, fontweight='bold')
    # plt.savefig('after.svg')
    # plt.show()
