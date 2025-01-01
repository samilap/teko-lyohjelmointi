import numpy as np

file_in = 'm4in.npz'
file_out = 'm4out.npy'

taulukkoz = np.load(file_in)
taulukko = taulukkoz['b']

np.save(file_out, taulukko)
