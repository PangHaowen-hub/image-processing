# show_pkl.py

import pickle

path = r'C:\Users\user\Desktop\model_best.model.pkl'


f = open(path, 'rb')

data = pickle.load(f)

print(data)

print(len(data))
