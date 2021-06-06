# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:01:04 2021

@author: elias
"""
import directory
from numpy import genfromtxt


from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main(jobid, files):
    data = genfromtxt(directory.Clustering(jobid) + "/mds.csv", delimiter=',')
    data = pd.DataFrame(data)
    db = DBSCAN(eps=0.3, min_samples=1).fit(data)
    y_pred = db.fit_predict(data)
    labels = db.labels_
    print(labels)
    # Number of clusters in labels, ignoring noise if present.
    
    unique_labels = set(labels)
    plt.figure()
    plt.scatter(data.iloc[:,0], data.iloc[:,1],c=y_pred, cmap='Paired')
    for i in range(0, len(files)):        
        filename = files[i][3:-12]
        plt.annotate(filename, (data.iloc[i][0]+2, data.iloc[i][1]+2))
    savedir = directory.Image_clustering(jobid) + "/dbscan.png"
    plt.savefig(savedir)
    