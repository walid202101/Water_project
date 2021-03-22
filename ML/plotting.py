# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:09:16 2021

@author: elias
"""
from pylab import plt
import numpy as np
# To plot:
# FCS File raw data
# Data after transformation
def scatter(channel1, channel2, data, filename):
    x = data[channel1]
    y = data[channel2]
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
    plt.xlabel(channel1)
    plt.ylabel(channel2)
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.savefig(filename + ".png")

# To plot:
# Generated HeatMap
# Gate
# diff
def heatmap(channel1, channel2, data, filename):
    plt.clf()
    plt.xlabel(channel1)
    plt.ylabel(channel2)     
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.savefig(filename + ".png")