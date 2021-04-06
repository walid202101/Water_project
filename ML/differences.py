#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Mar  3 00:54:51 2020

@author: dave

This code calculates the difference between gated samples according to the following:
1. It calculates the Hamming distance (can be modified to geometric if needed)
2. The calculated distances between each pair of files are saved in to a file.
3. The gated samples are read in the 'rawdatadir' folder (directory)
4. The input files are read into frames (matrices)
5. Each input file is expected to have equal number of rows and columns
6. The output files are stored in the 'diffdatadir' directory below 

The number of files is N(N-1)/2 where N is the number of samples in the directory
"""

####################################################    
"""
This function calculates the difference matrix of frames extracted from two data files.
The difference (absolute) is the distance between the frames.
If needed, the formula for geometric distance can be applied (Pythagorean) 
It then saves the resulting matrix to a file.
Name    = get_and_save_diff

Input arguments 
    Sample1     = file containing the gated data for the first sample
    Sample2     = filee containing the gated data for the second sample

Returns         = None
Used local variables    =
    dframe1     = data frame for sample1 
    dframe2     = data frame for sample2 
    numrows     = number of rows of data
    numcols     = number of columns in the data   
    dataxy1     = vector to read data from ith row of frame1
    dataxy2     = vector to read data from ith row of frame2
    diffArray   = 2D matrix for holding the difference between the corresponding 
    filename    = name of output file
"""

import pandas as pd 
import numpy as np
from numpy import genfromtxt
from pylab import plt

def main(dframe1, dframe2):    
    numrows = dframe1.shape[0]
    numcols = dframe1.shape[1]
    
    if(dframe2.shape[0]< dframe1.shape[0]):
        numrows = dframe2.shape[0]
        numcols = dframe2.shape[1]    
    
    diffArray = np.zeros((numrows, numcols), dtype=np.int32)
    for i in range(numrows):
       dataxy1 = dframe1[i]
       dataxy2 = dframe2[i]
       for j in range(numcols):
            diffArray[i][j] = abs(dataxy1[j] - dataxy2[j])
    # Plotting heatmap
    #plt.clf()   
    #plt.imshow(diffArray, cmap='hot', interpolation='nearest')
    
    return diffArray

def symmetrize(a):
    """
    Return a symmetrized version of NumPy array a.

    Values 0 are replaced by the array value at the symmetric
    position (with respect to the diagonal), i.e. if a_ij = 0,
    then the returned array a' is such that a'_ij = a_ji.

    Diagonal values are left untouched.

    a -- square NumPy array, such that a_ij = 0 or a_ji = 0, 
    for i != j.
    """
    return a + a.T - np.diag(a.diagonal())
