import os

path = r'G:\CT2CECT\data_nii'
for i in range(30):
    t = str(i).rjust(3, '0')
    os.mkdir(os.path.join(r'G:\CT2CECT\data_nii', t))
