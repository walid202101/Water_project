# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:37:31 2021

@author: elias
"""
from pylab import plt
import numpy as np

def plotting(channel1, channel2, data):
    plt.clf()
    plt.xlabel(channel1)
    plt.ylabel(channel2)     
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.show()
    
BINWIDTH = 1000

def gating(x1, x2, y1, y2, dataframe):
    gated = np.zeros((1+x2-x1, 1+y2-y1), dtype=np.uint16)
    for i in range(0,x2-x1):
        for j in range(0,y2-y1):
            gated[i][j] = dataframe[i+x1][j+y1]
            
    return gated
    
def generate_map(dframe, filename, channel1, channel2):
    numrows = dframe.shape[0]
    datax = dframe[channel1]
    xmax = max(datax)
    datax = dframe[channel2]
    ymax = max(datax)
    xbin = int(xmax/BINWIDTH) + 1
    ybin = int(ymax/BINWIDTH) + 1
    binArray = np.zeros((xbin, ybin), dtype=np.int32)
    
    #Generate heatmap by counting number of events in a bin, for each data row
    for i in range(numrows):
        dataxy = dframe.iloc[i]
        xval = int(dataxy[0] / BINWIDTH)
        yval = int(dataxy[1] / BINWIDTH)
        binArray[xval][yval] = 1 + binArray[xval][yval]
    return binArray
        
 