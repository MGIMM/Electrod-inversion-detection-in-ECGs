import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np


#function for data importing
def DataImporting():
    'Data importing : Xtrain, Ytrain & Xtest'
    Xtrain = pd.read_csv('raw data/input_training.csv',sep = ',',header = 0)
    Ytrain = pd.read_csv('raw data/output_training.csv',sep = ';',header = 0)
    Xtest = pd.read_csv('raw data/input_testing.csv',sep = ',',header = 0)
    return Xtrain,Ytrain,Xtest

#function for data sampling
def DataSample(X,ID,index):
    'X:dataframe of input data'
    'Id = id, from 0 to 999'
    'index = index of channel, from 1 to 12'
    return X.iloc[ID,1+(index-1)*750:1+index*750] 

#function for ploting Confusion Matrix.
def PlotCM(lable,pred,title):
    'Plot confusion matrix for supervised classification'
    cm = confusion_matrix(lable,pred)
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.imshow(cm_normalized, interpolation='nearest',cmap = 'OrRd')
    plt.title('Confusion Matrix for '+ title)
    plt.colorbar()
    for y in range(2):
        for x in range(2):
            plt.text(x, y , '%.2f' % cm[y,x],
                     horizontalalignment='center',
                     verticalalignment='center',
                     )
            
