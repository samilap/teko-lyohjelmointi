import numpy as np

filein = 'm2in.npy'
fileout = 'm2out.npy'

taulukko = np.load(filein)

taulukko[0,0] = 1

last_row_index = taulukko.shape[0] - 1
last_colum_index = taulukko.shape[1] - 1

taulukko[0,0] = 1
taulukko[last_row_index, last_colum_index] = -1

np.save(fileout, taulukko)