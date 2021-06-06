# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:54:09 2021

@author: elias
"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering

import directory
from numpy import genfromtxt

def main(jobid, files):
    data = genfromtxt(directory.Clustering(jobid) + "/mds.csv", delimiter=',')
    data = pd.DataFrame(data)
    cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
    cluster.fit(data)
    #predict = cluster.fit_predict(data)
    
    plt.figure()
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c=cluster.labels_, cmap='rainbow')
    for j in range(0, len(data)):
        filename = files[j][3:-12]
        plt.annotate(filename, (data.iloc[j][0]+2, data.iloc[j][1]+2))
    savedir = directory.Image_clustering(jobid) + "/hierarchical.png"
    plt.savefig(savedir)