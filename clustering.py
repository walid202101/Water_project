# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:27:48 2021

@author: elias
"""
import dbscan
import kmeans
import kmodes_
import hierarchical

from os import walk
import directory


import dbconnection
from flask import Flask
from flask import request
app = Flask(__name__)

# http://127.0.0.1:5002/clustering?jobid=2&clusteringmethod=dbscan
# http://127.0.0.1:5002/clustering?jobid=2&clusteringmethod=kmeans
# http://127.0.0.1:5002/clustering?jobid=2&clusteringmethod=kmodes
# http://127.0.0.1:5002/clustering?jobid=2&clusteringmethod=hierarchical

@app.route('/clustering')
def main():
    jobid = request.args.get('jobid')
    clusteringmethod = request.args.get('clusteringmethod')
    # Reading file from directory
    files = []
    for (dirpath, dirnames, filenames) in walk(directory.Fcs_files(jobid)):
        files.extend(filenames)
        
    if(clusteringmethod == 'dbscan'):    
        dbscan.main(jobid, files)
    elif(clusteringmethod == 'kmeans'):
        kmeans.main(jobid, files)
    elif(clusteringmethod == 'kmodes'):
        kmodes_.main(jobid, files)
    elif(clusteringmethod == 'hierarchical'):
        hierarchical.main(jobid, files)
    
    # Update database
    returnmessage = dbconnection.main(jobid, 3)
    return returnmessage


if __name__ == '__main__':
   app.run(port=5002)
   
