import sys
import time
import pandas

inputfile='weather_data.csv'
outputfile='preprocessed.csv'

data=pandas.read_csv(inputfile)

#Your code here

data.to_csv(outputfile)
