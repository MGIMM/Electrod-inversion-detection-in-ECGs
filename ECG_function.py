import pandas as pd


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
    'Id = id, from 0 to 4'
    'index = index of channel, from 1 to 12'
    return X.iloc[ID,1+(index-1)*750:1+index*750] 

