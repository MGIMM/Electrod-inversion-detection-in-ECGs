import pandas as pd
from matplotlib import pyplot as plt


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

#function for ploting
def PlotAllChannels (X,ID):
    fig, ((ax1, ax2, ax3), (ax4, ax5,ax6),(ax7, ax8, ax9), (ax10, ax11,ax12)) = plt.subplots(4, 3, sharex='col', sharey='row')
    fig.set_size_inches(15, 15)
    for (ax,i) in zip((ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12),range(1,13,1)):
        ax.plot(DataSample(X,ID,i))
        ax.set_title('channel '+str(i))
    return True    
    