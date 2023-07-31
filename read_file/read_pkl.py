import pickle

path = r'F:\my_code\SynthRAD2023\nnUNet\nnUNet_preprocessed\Dataset101_SynthRAD\nnUNetPlans_3d_fullres\1BA001.pkl'


f = open(path, 'rb')

data = pickle.load(f)

print(data)

print(len(data))
