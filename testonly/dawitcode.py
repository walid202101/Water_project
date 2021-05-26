# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:17:14 2021

@author: elias
"""
import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn import manifold
from numpy import genfromtxt
from pylab import plt

def main():
    car = np.random.randint(2, size=(100,5))
    print(car.shape)
    #Diff
    dis_matrix = pairwise_distances(car, metric='jaccard')
    print(dis_matrix.shape)
    print(type(dis_matrix))
    
    
    #
    mds_model = manifold.MDS(n_components=2, random_state=0, dissimilarity='precomputed')
    mds_fit = mds_model.fit(dis_matrix)
    
    mds_coors = mds_model.fit_transform(dis_matrix)
    
    plt.figure()
    plt.scatter(mds_coors[:,0], mds_coors[:,1], facecolors = 'green',edgecolors='none')
    plt.show()
    
main()