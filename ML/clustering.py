# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:27:48 2021

@author: elias
"""

import directory
import dbscan
import kmeans
import kmodes_
import hierarchical

from flask import Flask
from flask import request
app = Flask(__name__)
#http://127.0.0.1:5000/dbscan?jobid=1

@app.route('/dbscan')
def main1():
    jobid = request.args.get('jobid')
    dbscan.main(jobid)
    return 'Done: dbscan'

#http://127.0.0.1:5000/kmeans?jobid=1
@app.route('/kmeans')
def main2():
    jobid = request.args.get('jobid')
    kmeans.main(jobid)
    return 'Done: kmeans'

#http://127.0.0.1:5000/kmodes?jobid=1
@app.route('/kmodes')
def main3():
    jobid = request.args.get('jobid')
    kmodes_.main(jobid)
    return 'Done: kmodes'

#http://127.0.0.1:5000/hierarchical?jobid=1
@app.route('/hierarchical')
def main4():
    jobid = request.args.get('jobid')
    hierarchical.main(jobid)
    return 'Done: hierarchical'

if __name__ == '__main__':
   app.run()
   
