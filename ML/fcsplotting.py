# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:55:13 2021

@author: elias
"""
import sys
from FlowCytometryTools import FCMeasurement
from pylab import plt
import numpy as np


def main(channel1, channel2, input_file_name, output_file_name):
    data = FCMeasurement(ID=input_file_name, datafile=input_file_name)
    x = data[channel1]
    y = data[channel2]
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
    plt.xlabel(channel1)
    plt.ylabel(channel2)
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.savefig(output_file_name + ".png")
    
"""  
channel1 = sys.argv[0]
channel2 = sys.argv[1]
inputfile = sys.argv[2]
outputfile = sys.argv[3]
"""

channel1 = 'FL1-H'
channel2 = 'FL3-H'
inputfile = 'fcs_files/A02 Kranvatten Augusti SYBR.fcs'
outputfile = 'A02 Kranvatten Augusti'

main(channel1, channel2, inputfile, outputfile)