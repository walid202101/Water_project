# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:51:48 2021

@author: elias
"""
import pandas as pd
from sklearn.cluster import KMeans
from pylab import plt
import numpy as np



def main():
    n_digits = 4
    data = pd.read_csv("FinalData/data.csv")
    kmeans = KMeans(init="random", n_clusters=n_digits, n_init=4, random_state=0)
    df = kmeans.fit_transform(data)
    label = kmeans.fit_predict(df)


    centroids = kmeans.cluster_centers_
    u_labels = np.unique(label)
    print(centroids)
    #Getting the Centroids

 
    #plotting the results:
    plt.figure()
    for i in u_labels:
        plt.scatter(df[label == i , 0] , df[label == i , 1] , label = i, s=10)
    plt.scatter(centroids[:,0] , centroids[:,1] , s = 30, color = 'k')
    plt.legend()
    plt.show()

    
    
    


main()