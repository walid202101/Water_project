# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:36:04 2021

@author: elias


# input FCS File, Output Pandas dataframe
"""
# TO DO: Add method to save plot 
import sys
from FlowCytometryTools import FCMeasurement
import numpy as np
from pylab import plt




def main(channel1, channel2, inputfile, outputfile, transformed_method, b):
    
    data = FCMeasurement(ID=inputfile, datafile=inputfile)
    # Transformations
    # The presence of both very dim and very bright cell populations in flow cytometry data can make
    # it difficult to simultaneously visualize both populations on the same plot. To address this problem,
    # flow cytometry analysis programs typically apply a transformation to the data to make it easy to visualize and
    # interpret properly. Rather than having this transformation applied automatically and without your knowledge,
    # this package provides a few of the common transformations (e.g., hlog, tlog), but ultimately leaves it up to you
    # to decide how to manipulate your data.
    data = data.transform(
        transformed_method,
        channels=[channel1, channel2],
        b=b)
    
    tranformed_data = data.data[[channel1, channel2]]
    tranformed_data.to_csv(outputfile + ".csv")
    
    # Plotting
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

    
"""
channel1 = sys.argv[0]
channel2 = sys.argv[1]
inputfile = sys.argv[2]
outputfile = sys.argv[3]
transformed_method = sys.argv[4]
b = sys.argv[5] 
"""

channel1 = 'FL1-A'
channel2 = 'FL3-A'
inputfile = 'fcs_files/A02 Kranvatten kvall SYBR.fcs'
outputfile = 'A02 Kranvatten kvall'
transformed_method = 'hlog'
b = 500

main(channel1, channel2, inputfile, outputfile, transformed_method, b)
    
    