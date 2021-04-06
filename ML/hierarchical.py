# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:54:09 2021

@author: elias
"""
import pandas as pd
from pylab import plt
import matplotlib.cm as cm

import numpy as np
from sklearn.cluster import AgglomerativeClustering

import directory
from numpy import genfromtxt

def main(jobid):
    data = genfromtxt(directory.Clustering(jobid) + "/mds.csv", delimiter=',')
    data = pd.DataFrame(data)
    cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
    cluster.fit(data)
    predict = cluster.fit_predict(data)
    
    plt.figure()
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c=cluster.labels_, cmap='rainbow')
    savedir = directory.Image_clustering(jobid) + "/hierarchical.png"
    plt.savefig(savedir)