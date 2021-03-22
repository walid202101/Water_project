# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:02:12 2021

@author: elias
"""
import numpy as np
import sys
import pandas as pd
from pylab import plt

 
def main(x1, x2, y1, y2, inputfile, outputfile):
    data = pd.read_csv(inputfile + ".csv")
    gated = np.zeros((1+x2-x1, 1+y2-y1), dtype=np.uint16)
    for i in range(0,x2-x1):
        for j in range(0,y2-y1):
            gated[i][j] = data[i+x1][j+y1]
            
    np.savetxt(outputfile + ".csv", delimiter=",")
    
    # Plotting heatmap
    plt.clf()   
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.savefig(outputfile + ".png")


x1 = sys.argv[0]
x2 = sys.argv[1]
y1 = sys.argv[2]
y2 = sys.argv[3]
inputfile = sys.argv[4]
outputfile = sys.argv[5]

main(x1, x2, y1, y2, inputfile, outputfile)