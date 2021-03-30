# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:02:12 2021

@author: elias
"""
import numpy as np
from numpy import genfromtxt
import pandas as pd
from pylab import plt
import seaborn as sb

import mysql.connector
import directory
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/gating')  
 
def main():
    inputfile = directory.heatmap_path(request.args.get('inputfile'))
    outputfile = directory.gates_path(request.args.get('outputfile'))
    print(inputfile)
    # This part should be replace by correct params 
    x1 = int(request.args.get('y1'))
    x2 = int(request.args.get('y2'))
    
    y1 = int(request.args.get('x1'))
    y2 = int(request.args.get('x2'))
    
    data = genfromtxt(inputfile + '.csv', delimiter=',')
    size = 1 + x2 - x1
    if(1+y2-y1> size):
        size = 1 + y2-y1
    gated = np.zeros((size, size), dtype=np.uint16)
    for i in range(0,x2-x1):
        for j in range(0,y2-y1):
            gated[i][j] = data[i+x1][j+y1]
            
    np.savetxt(outputfile + ".csv",gated, delimiter=",")
    print(gated.shape)
    print(gated)
    print("------------")
    
    fig, ax = plt.subplots(figsize=(11, 9))
    sb.heatmap(gated)
    
    plt.savefig(outputfile + ".png")
    plt.show()
    
    return 'Done'

if __name__ == '__main__':
   app.run()