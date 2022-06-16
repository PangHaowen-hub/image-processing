import numpy as np
import SimpleITK as sitk

data = np.load(r'C:\Users\user\Desktop\lobe512_000.npz')
x = data['softmax']
x0 = np.mean(x[1:], axis=0)
np.savez(r"C:\Users\user\Desktop\lobe512_000_new0.npz", x0)

x1 = np.sum(x[1:], axis=0)
np.savez(r"C:\Users\user\Desktop\lobe512_000_new1.npz", x1)

x2 = np.max(x[1:], axis=0)
np.savez(r"C:\Users\user\Desktop\lobe512_000_new2.npz", x2)

