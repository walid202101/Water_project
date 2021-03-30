# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:55:13 2021

@author: elias
"""
import sys
from FlowCytometryTools import FCMeasurement
from pylab import plt
import numpy as np

import mysql.connector
import directory
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/fcsplotting')  

def main():
    inputfile = directory.fcsfiles_path(request.args.get('inputfile'))
    outputfile = directory.fcsfiles_path(request.args.get('outputfile'))
    channel1=request.args.get('channel1')
    channel2=request.args.get('channel2')
    
    data = FCMeasurement(ID=inputfile, datafile=inputfile)
    x = data[channel1]
    y = data[channel2]
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
    plt.xlabel(channel1)
    plt.ylabel(channel2)
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.savefig(outputfile + ".png")
    
    return 'Done'

if __name__ == '__main__':
   app.run()

