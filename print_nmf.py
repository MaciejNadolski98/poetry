import numpy as np
import pickle

# array_loaded = np.load('p_nmf_en_d100.npy')
# print(array_loaded[-4:], array_loaded.shape)

with open('nmf_en_descriptions_d100.pickle', 'rb') as f:
    obj = pickle.load(f)
print(obj)