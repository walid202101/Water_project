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

import mysql.connector
from flask import Flask
from flask import request
app = Flask(__name__)

# http://127.0.0.1:5002/clustering?jobid=1&clusteringmethod=dbscan
# http://127.0.0.1:5002/clustering?jobid=1&clusteringmethod=kmeans
# http://127.0.0.1:5002/clustering?jobid=1&clusteringmethod=kmodes
# http://127.0.0.1:5002/clustering?jobid=1&clusteringmethod=hierarchical

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
    
    try:
     connection = mysql.connector.connect(host='localhost',
                                         database='water_project',
                                         user='root',
                                         password='')
    
     cursor = connection.cursor()

     job_status="COMPLETED"
     cursor.execute ("""
     UPDATE jobs
     SET job6_status=%s
     WHERE job_id=%s
     """, (job_status,jobid))

     connection.commit()
     print(cursor.rowcount, "Record Update successfully into jobs")
     cursor.close()

    except mysql.connector.Error as error:
     print("Failed to insert record into table {}".format(error))

    finally:
     if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

    return 'clustering job completed'


if __name__ == '__main__':
   app.run(port=5002)
   
