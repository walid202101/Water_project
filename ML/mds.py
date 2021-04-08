"""
Created on Wed Mar 24 12:02:38 2021

@author: elias
"""
import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn import manifold
from numpy import genfromtxt
from pylab import plt
import pandas as pd
import directory

def main(files, data, size, jobid):
        # Reduce scaling        
    mds =manifold.MDS(n_components=2, random_state=123, dissimilarity='precomputed')
    croods = mds.fit_transform(data)
    
    centriods = []
    for i in range(0,len(files)):
        subarray = croods[i*size : i*size +size]
        centriods.append(subarray.mean(axis=0))
    centriods = np.array(centriods)
    savedir = directory.Clustering(jobid) + "/mds.csv"
    np.savetxt(savedir, centriods, delimiter=",")
    
    plt.figure()
    #plt.xlim(-100, 100)
    #plt.ylim(-100, 100)
    for i in range(0, len(centriods)):
        plt.scatter(centriods[i][0], centriods[i][1], marker='x', s=10)
        filename = files[i][3:-12]
        plt.annotate(filename, (centriods[i][0]+2, centriods[i][1]+2))
    plt.savefig(directory.Image_differences(jobid) + "/mds.png")
      
