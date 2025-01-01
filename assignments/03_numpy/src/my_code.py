import numpy as np

file_a = 'a.npy'
file_b = 'b.npy'
file_ab = 'ab.npz'

a = np.load(file_a)
b = np.load(file_b)

np.savez(file_ab, a=a, b=b)
