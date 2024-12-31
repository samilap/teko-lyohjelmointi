import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

inputfile='in.npy'
outputfile='out.npy'

data=np.load(inputfile)

#Your code here

np.save(outputfile, packed_data)
