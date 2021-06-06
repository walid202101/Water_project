# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:19:31 2021

@author: elias
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np
from kmodes.kmodes import KModes

import directory
from numpy import genfromtxt


def main(jobid, files):
    data = genfromtxt(directory.Clustering(jobid) + "/mds.csv", delimiter=',')
    data = pd.DataFrame(data)
    km = KModes(n_clusters=2, init='Huang', n_init=5, verbose=0)
    df = km.fit_predict(data)
    centroids = km.cluster_centroids_
    
    data['df'] = df
    
    u_labels = np.unique(df)

    colors = cm.rainbow(np.linspace(0, 1, len(u_labels)))
    #plotting the results:
    plt.figure()
    colors = ['red', 'green', 'blue', 'orange']
    
    for i in u_labels:
        subdata = data.loc[data['df'] == i]
        plt.scatter(subdata.iloc[:,0] , subdata.iloc[:,1] , label = i, s=10, color=colors[i])
    print(data.iloc[0][0])  
    for j in range(0, len(data)):
        filename = files[j][3:-12]
        plt.annotate(filename, (data.iloc[j][0]+2, data.iloc[j][1]+2))
    plt.scatter(centroids[:,0] , centroids[:,1] , s = 30, color = 'k')
    plt.legend()
    savedir = directory.Image_clustering(jobid) + "/kmodes.png"
    plt.savefig(savedir)
    