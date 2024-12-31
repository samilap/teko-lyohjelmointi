import pandas
from scipy import stats
import numpy as np
from sklearn import preprocessing

inputfile='time_series.csv'
trainfile='train.csv'
testfile='test.csv'

data=pandas.read_csv(inputfile)

#Your code here

#Save train data
print("Save train data")
traindata.to_csv(trainfile)

#Save test data
print("Save test data")
testdata.to_csv(testfile)

