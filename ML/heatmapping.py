# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:37:31 2021

@author: elias
"""
import numpy as np
import pandas as pd
from pylab import plt
import seaborn as sb

import mysql.connector
import directory
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/heatmapping')  

def main():
    inputfile = directory.transform_path(request.args.get('inputfile'))
    outputfile = directory.heatmap_path(request.args.get('outputfile'))
    channel1=request.args.get('channel1')
    channel2=request.args.get('channel2')
    binwidth = int(request.args.get('binwidth'))
    print(inputfile)
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
        xval = int(dataxy[1] / binwidth)
        yval = int(dataxy[2] / binwidth)
        binArray[xval][yval] = 1 + binArray[xval][yval]
    np.savetxt(outputfile + ".csv",binArray, delimiter=",")
    print(binArray.shape)
    
    
    fig, ax = plt.subplots(figsize=(11, 9))
    sb.heatmap(binArray)
    
    plt.savefig(outputfile + ".png")
    plt.show()
    return 'Done'


if __name__ == '__main__':
   app.run()