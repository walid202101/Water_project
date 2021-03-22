# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:37:31 2021

@author: elias
"""
import numpy as np
import pandas as pd
from pylab import plt

import sys

def main(channel1, channel2, inputfile, outputfile, binwidth):
    data = pd.read_csv(inputfile + ".csv")
    numrows = data.shape[0]
    datax = data[channel1]
    xmax = max(datax)
    datax = data[channel2]
    ymax = max(datax)
    xbin = int(xmax/binwidth) + 1
    ybin = int(ymax/binwidth) + 1
    binArray = np.zeros((xbin, ybin), dtype=np.int32)
    
    #Generate heatmap by counting number of events in a bin, for each data row
    for i in range(numrows):
        dataxy = data.iloc[i]
        xval = int(dataxy[0] / binwidth)
        yval = int(dataxy[1] / binwidth)
        binArray[xval][yval] = 1 + binArray[xval][yval]
    pd.DataFrame.to_csv(outputfile + ".csv")
    
    # Plotting heatmap
    plt.clf()
    plt.xlabel(channel1)
    plt.ylabel(channel2)     
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.savefig(outputfile + ".png")



channel1 = sys.argv[0]
channel2 = sys.argv[1]
inputfile = sys.argv[2]
outputfile = sys.argv[3]
binwidth = sys.argv[4]
main(channel1, channel2, inputfile, outputfile, binwidth)

 