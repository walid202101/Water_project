# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:02:12 2021

@author: elias
"""
import numpy as np
from numpy import genfromtxt
import sys
import pandas as pd
from pylab import plt

 
def main(x1, x2, y1, y2, inputfile, outputfile):
    data = genfromtxt(inputfile + '.csv', delimiter=',')
    gated = np.zeros((1+x2-x1, 1+y2-y1), dtype=np.uint16)
    for i in range(0,x2-x1):
        for j in range(0,y2-y1):
            gated[i][j] = data[i+x1][j+y1]
            
    np.savetxt(outputfile + ".csv",gated, delimiter=",")
    
    # Plotting heatmap
    plt.clf()   
    plt.imshow(gated, cmap='hot', interpolation='nearest')
    plt.savefig(outputfile + ".png")

"""
x1 = sys.argv[0]
x2 = sys.argv[1]
y1 = sys.argv[2]
y2 = sys.argv[3]
inputfile = sys.argv[4]
outputfile = sys.argv[5]
"""

x1 = 0
x2 = 15
y1 = 12
y2 = 23
inputfile = 'A02 Kranvatten kvall'
outputfile = 'A02 Kranvatten kvall46'

main(x1, x2, y1, y2, inputfile, outputfile)