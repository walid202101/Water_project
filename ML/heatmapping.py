# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:37:31 2021

@author: elias
"""
import numpy as np
from pylab import plt
import seaborn as sb
import directory

def main(data, channel1, channel2, binwidth, filename, jobid):    
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
    
    fig, ax = plt.subplots(figsize=(11, 9))
    sb.heatmap(binArray, cmap='YlGnBu')
    plt.title("heatmap for " + filename)
    savedir = directory.Image_heatmap(jobid) + "/" + filename + '.png'
    plt.savefig(savedir)
    
    return binArray