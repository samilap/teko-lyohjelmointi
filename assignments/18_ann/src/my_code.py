from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

#Just for help...
def plot(x, y):
    plt.subplot(2,1,1)
    plt.scatter(x[:, 0], x[:, 1], c=y[:, 0], marker='.')
    plt.title('y[:, 0]')
    plt.colorbar()
    plt.subplot(2,1,2)
    plt.scatter(x[:, 0], x[:, 1], c=y[:, 1], marker='.')
    plt.title('y[:, 1]')
    plt.colorbar()

#Predict value(s) of the function
def compute_value(x):
    global model
    return model.predict(x)


def init_model():
    global model #Model variable
    x=np.load('x.npy')
    y=np.load('y.npy')

    #NOTE: All data is in x and y    
    
    #Split data into test and train sets. Use 15000 samples in train set.
    #Modify lines below
    x_train=None 
    x_test=None
    y_train=None
    y_test=None

    #Create model (network). Insert more lines if required.        
    model=None


    
    #print model information
    model.summary()
    
    #Compile model, choose loss function. Model line below
    model.compile(loss=None, optimizer='adam')
    
    #Teach model. Insert required parameters
    history = model.fit()

    #plt.plot(history.history['loss'])
    #plt.semilogy()
    #plt.show()

    return x_test, y_test


if __name__ == "__main__":
    x_test, y_test=init_model()

    y_pred=compute_value(x_test)
    plot(x_test, y_pred)
    plt.show()

    print("MSE =", mean_squared_error(y_test ,y_pred))
