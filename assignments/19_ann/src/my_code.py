import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

Y_column=8

def splitXY(d):
    return d.drop(Y_column, axis=1), d[Y_column] 

data=pd.read_csv('traindata.csv', header=None)




#Your code here...




model.save('kotilo.keras')

predY=np.round(model.predict(testX)).reshape((n_test, ))

accepted_n=(np.abs(predY-testY)<=3).sum()
print('Correct predictions:', accepted_n, '/', n_test);

