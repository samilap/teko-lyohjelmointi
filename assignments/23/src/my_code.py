#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:31:48 2022

@author: kojape
"""

import pandas as pd
import numpy as np

def splitXY(d):
    Y_column='DEATH_EVENT'
    return d.drop(Y_column, axis=1).to_numpy(), np.int32(d[Y_column]) 


def load_data(filename):
    global drop_columns
    data=pd.read_csv(filename)
    #set random order
    data=data.sample(frac=1).reset_index(drop=True)
    for col in drop_columns:
        data.drop(col, axis=1, inplace=True)

    return data    

def init_model(datafile):
    
    global model
    global drop_columns
    
    #Modify this to drop unused columns from data
    drop_columns=[]

    data=load_data(datafile)



    #your code here
    # - Preprocess data
    # - Split data into two pieces; train set and test set
    # - Create and train model
    # - y_test shall contain values 1/0




    return x_test, y_test #return test set

    

#input x is unscaled
def compute_value(x):
    global model


    #your code here

    
    return pred_y


def validate(filename):
    data_val=load_data(filename)
    x_val, y_val=splitXY(data_val)
    y_pred=compute_value(x_val)
    return y_pred, y_val

if __name__ == "__main__":
    x_test, y_test=init_model('train.csv')

    testN, _=np.shape(x_test)
    assert(np.shape(y_test)==(testN,))

    y_pred=compute_value(x_test)
    errors=(y_pred!=y_test).sum()
    print('Errors (test set):', errors, '/', testN)


    #Just for testing that test.py will work 
    y_pred, y_val=validate('train.csv')
    valN=np.shape(y_val)[0]
    errors=(y_pred!=y_val).sum()
    #print('Errors (validation set):', errors, '/', valN)


    
    
