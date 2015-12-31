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
            

def neighbour(newobj,listindex,threshold = 10):
    for obj in listindex:
        if np.abs(newobj-obj)<threshold:
            return True
#function for PeriodSplit

def PeriodSplit(wave,threshold =1.0/10):
    set_peak = [np.argmax(np.abs(wave[:300]))]
    max_peak = wave[set_peak[0]]
    for i in range(len(wave)):
        if np.abs(wave[i]-max_peak) <= 1.0/4*np.abs(max_peak) and neighbour(i,set_peak) != True :
            set_peak.append(i)
    num_peak = len(set_peak)     
    start_interval = range(np.min(set_peak))
    

    
    
    if num_peak == 1 or num_peak == 2 or num_peak>5:
        
        num_peak = 3     
        start_interval = range(50)
        
        
        
    period_interval = range(750/(num_peak+1),750/(num_peak-1),1)
    sd = [[[]for period in period_interval] for start in start_interval]
    for start in start_interval:
        for period in period_interval:
            if np.abs(wave[start])<threshold*np.abs(np.max(wave)) and start + period*2<750:
                sd[start][period-period_interval[0]] = np.std(wave[start:start+period]-wave[start+period:start+period*2])
            else:
                sd[start][period-period_interval[0]] = float('inf')

    sdlist = []
    for start in sd:
        sdlist += start
    start,period = np.argmin(sd)/len(period_interval),np.argmin(sd)%len(period_interval)+period_interval[0]
    
    print "number of peaks : ",num_peak
    print "start at :", start
    print 'period :', period
    return wave[start :start + period]

