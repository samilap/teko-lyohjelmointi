import sys
import time
import numpy as np
from sklearn.decomposition import PCA
from keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

reduced_N=32

########################################################
#Write your code here

#Set value range -1..1


#Convert figures to vectors

#Compute reduced PCA

train_X_packed=... #reduced dimension
test_X_packed=... #reduced dimension

#End of your code
########################################################
#Do not modify lines below this point!




#Save packed data
print('Save packed data')
np.save('packed_train.npy', train_X_packed)
np.save('packed_test.npy', test_X_packed)

if len(sys.argv)==1:
    #Test quality
    print('Train model')
    model = KNeighborsClassifier(n_neighbors = 11)
    model.fit(train_X_packed, train_Y)

    print('Compute predictions')
    pred = model.predict(test_X_packed)
    acc = accuracy_score(test_Y, pred)

    print('Accuracy =',acc)
