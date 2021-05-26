# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:03:30 2021

@author: elias
"""

from os import walk

import differences
import mds

from numpy import genfromtxt

import matplotlib.pyplot as plt
import seaborn as sb

import numpy as np

import directory
import dbconnection


from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/diff')
#http://127.0.0.1:5001/diff?jobid=2

def main():
    jobid = request.args.get('jobid')
    # Reading file from directory
    files = []
    
    numberoffile = 0
    squaresize = 0
    for (dirpath, dirnames, filenames) in walk(directory.Gating(jobid)):
        files.extend(filenames) 
    dataset = []
    for file in files:
        filepath = directory.Gating(jobid) + "/" + file
        tempdata = genfromtxt(filepath, delimiter=',')
        dataset.append(tempdata)
    numberoffile = len(dataset)
    # Calculate Differecne
    savedir = directory.Differences(jobid)
    
    diff = []
    for i in range(numberoffile):
        subdiff = []
        for j in range(numberoffile):
            diffarr = differences.main(dataset[i], dataset[j])
            subdiff.append(diffarr)
            
            # Save file & plot
            filename = directory.Differences(jobid) + "/diff_"+ str(i) + "_"+str(j) + "_" + ".csv"
            plotname = directory.Image_differences(jobid) + "/diff_"+ str(i) + "_"+str(j) + "_" + ".png"
            np.savetxt(filename, diffarr, delimiter=",")
            if(i!=j):
                plt.figure()
                sb.heatmap(diffarr, cmap='YlGnBu')
                plt.savefig(plotname)
            
        diff.append(subdiff)
    diff = np.array(diff)
    print(diff.shape)
    
    squaresize = diff.shape[2]
    w, h = numberoffile * squaresize, numberoffile * squaresize
    # Transform the diff array into on diff array of shape w, h
    bucket = [[0] * w for i in range(h)]
    bucket = np.array(bucket)
    for i in range(numberoffile):
        for j in range(numberoffile):
            for k in range(squaresize):
                for l in range(squaresize):
                    bucket[(i*squaresize)+k,(j*squaresize)+l] = diff[i][j][k][l]
    
    
    # save in diff
    savedir = directory.Differences(jobid) + "/diff.csv"
    np.savetxt(savedir, bucket, delimiter=",")
    
    bucket = differences.symmetrize(bucket)
    
    plt.figure()
    sb.heatmap(bucket, cmap='YlGnBu')
    plt.savefig(directory.Image_differences(jobid) + "/diff.png")
    
    # MDS Implementation
    mds.main(files, bucket, squaresize, jobid)           

    # Update database
    returnmessage = dbconnection.main(jobid, 2)
    return returnmessage
    
if __name__ == '__main__':
   app.run(port=5001)