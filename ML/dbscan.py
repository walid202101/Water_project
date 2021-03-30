# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:01:04 2021

@author: elias
"""

from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def main():
    data = pd.read_csv("FinalData/data.csv")
    db = DBSCAN(eps=0.3, min_samples=10).fit(data)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    
    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = 2
    n_noise_ = list(labels).count(-1)
    
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
    plt.figure()
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]
    
        class_member_mask = (labels == k)
    
        #xy = data[class_member_mask & core_samples_mask]
        #plt.plot(xy.iloc[:, 0], xy.iloc[:, 1])
    
        xy = data[class_member_mask & ~core_samples_mask]
        plt.plot(xy.iloc[:, 0], xy.iloc[:, 1])
    plt.show()
    
main()