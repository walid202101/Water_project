# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:02:12 2021

@author: elias
"""
import numpy as np
from numpy import genfromtxt
import pandas as pd
import directory
from pylab import plt
import seaborn as sb

 
def main(data, x1, x2, y1, y2, filename, jobid):    
    size = 1 + x2 - x1
    if(1+y2-y1> size):
        size = 1 + y2-y1
    gated = np.zeros((size, size), dtype=np.uint16)
    for i in range(0,x2-x1):
        for j in range(0,y2-y1):
            gated[i][j] = data[i+x1][j+y1]
        
    
    fig, ax = plt.subplots(figsize=(11, 9))
    sb.heatmap(gated, cmap='YlGnBu')
    plt.title("gating for " + filename)
    savedir = directory.image_gating(jobid) + "/" + filename + '.png'
    plt.savefig(savedir)
    
    return gated