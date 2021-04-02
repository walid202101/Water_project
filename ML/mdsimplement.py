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


def main(data):
    for i in range(0,len(data)):
        data[i] = symmetrize(data[i])
    mds =manifold.MDS(n_components=2, random_state=1, dissimilarity='euclidean')
    mds_croods = []
    for i in data:
        mds_crood = mds.fit_transform(i)         
        centroid = mds_crood.mean(axis=0)
        mds_croods.append(centroid)
    color = ['blue', 'green', 'red', 'pink', 'grey', 'yellow']
    plt.figure()
    for i in range(0, len(mds_croods)):
        plt.scatter(mds_croods[i][0], mds_croods[i][1], marker='x', s=20)
    plt.show()

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