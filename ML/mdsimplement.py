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

def main(inputfile1, inputfile2):
    
    inputfile1 = 'Diff/101'
    inputfile2 = 'Diff/102'
    inputfile3 = 'Diff/103'
    inputfile4 = 'Diff/104'
    inputfile5 = 'Diff/105'
    inputfile6 = 'Diff/106'
    
    dframe1 = genfromtxt(inputfile1 + '.csv', delimiter=',')
    dframe2 = genfromtxt(inputfile2 + '.csv', delimiter=',')
    dframe3 = genfromtxt(inputfile3 + '.csv', delimiter=',')
    dframe4 = genfromtxt(inputfile4 + '.csv', delimiter=',')
    dframe5 = genfromtxt(inputfile5 + '.csv', delimiter=',')
    dframe6 = genfromtxt(inputfile6 + '.csv', delimiter=',')

    dframe1 = symmetrize(dframe1)
    dframe2 = symmetrize(dframe2)
    dframe3 = symmetrize(dframe3)
    dframe4 = symmetrize(dframe4)
    dframe5 = symmetrize(dframe5)
    dframe6 = symmetrize(dframe6)
    
    dframe1 = dframe1.astype(int)
    dframe2 = dframe2.astype(int)
    dframe3 = dframe3.astype(int)
    dframe4 = dframe4.astype(int)
    dframe5 = dframe5.astype(int)
    dframe6 = dframe6.astype(int)
    

    
    
    mds =manifold.MDS(n_components=2, random_state=123, dissimilarity='precomputed')
    #mds_fit = mds.fit(dframe1)
    mds_crood1 = mds.fit_transform(dframe1)
    mds_crood2 = mds.fit_transform(dframe2)
    mds_crood3 = mds.fit_transform(dframe3)
    mds_crood4 = mds.fit_transform(dframe4)
    mds_crood5 = mds.fit_transform(dframe5)
    mds_crood6 = mds.fit_transform(dframe6)
    dat = []
    dat.append(pd.DataFrame(mds_crood1))
    dat.append(pd.DataFrame(mds_crood2))
    dat.append(pd.DataFrame(mds_crood3))
    dat.append(pd.DataFrame(mds_crood4))
    dat.append(pd.DataFrame(mds_crood5))
    dat.append(pd.DataFrame(mds_crood6))
    
    data = pd.concat(dat, ignore_index=True)
    data.to_csv("FinalData/data.csv", index=False)
    
    
    plt.figure()
    plt.scatter(mds_crood1[:,0], mds_crood1[:,1], facecolors = 'blue', edgecolors='none', s=20)
    plt.scatter(mds_crood2[:,0], mds_crood2[:,1], facecolors = 'green', edgecolors='none', s=20)
    plt.scatter(mds_crood3[:,0], mds_crood3[:,1], facecolors = 'red', edgecolors='none', s=20)
    plt.scatter(mds_crood4[:,0], mds_crood4[:,1], facecolors = 'pink', edgecolors='none', s=20)
    plt.scatter(mds_crood5[:,0], mds_crood5[:,1], facecolors = 'grey', edgecolors='none', s=20)
    plt.scatter(mds_crood6[:,0], mds_crood6[:,1], facecolors = 'yellow', edgecolors='none', s=20)
    plt.label()
    
    plt.show()
    
    
    """
    for label, x, y in zip(labels, mds_crood[:,0], mds_crood[:,1]):
        plt.annotate(labels, (x,y), xycoords='data')
        plt.xlabel('1st Dimension')
        plt.ylabel('2nd Dimension')
        plt.show()
    """
    

inputfile1 = 'Diff/Kranvatten AugKvall'
inputfile2 = 'Diff/Kranvatten AugKvall'
main(inputfile1, inputfile2)