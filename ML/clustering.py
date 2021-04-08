# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:27:48 2021

@author: elias
"""
import dbscan
import kmeans
import kmodes_
import hierarchical

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
    if(clusteringmethod == 'dbscan'):    
        dbscan.main(jobid)
    elif(clusteringmethod == 'kmeans'):
        kmeans.main(jobid)
    elif(clusteringmethod == 'kmodes'):
        kmodes_.main(jobid)
    elif(clusteringmethod == 'hierarchical'):
        hierarchical.main(jobid)
    
    # Update database
    returnmessage = dbconnection.main(jobid, 2)
    return returnmessage


if __name__ == '__main__':
   app.run(port=5002)
   
