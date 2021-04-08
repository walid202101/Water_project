# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 08:02:03 2021

@author: elias
"""
from os import walk

import transformation
import heatmapping
import gating
import mysql.connector
from FlowCytometryTools import FCMeasurement
import numpy as np
import directory
import mysql.connector

from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/fileprocessing')

# Test with this link
# http://127.0.0.1:5000/fileprocessing?jobid=1&channel1=FL1-A&channel2=FL3-A&transformed_method=hlog&b=100&binwidth=100&x1=18&x2=34&y1=32&y2=40

def main():
    # Reading the parameters
    jobid = request.args.get('jobid')
    channel1=request.args.get('channel1')
    channel2=request.args.get('channel2')
    transformed_method = request.args.get('transformed_method')
    b = int(request.args.get('b'))
    binwidth = int(request.args.get('binwidth'))
    
    # This part should be replace by correct params 
    x1 = int(request.args.get('y1'))
    x2 = int(request.args.get('y2'))
    y1 = int(request.args.get('x1'))
    y2 = int(request.args.get('x2'))
      
    # Reading file from directory
    files = []
    for (dirpath, dirnames, filenames) in walk(directory.Fcs_files(jobid)):
        files.extend(filenames) 
        
    dataset = []
    for file in files:
        filepath = directory.Fcs_files(jobid) + "/" + file
        tempdata = FCMeasurement(ID=file, datafile=filepath)
        dataset.append(tempdata)
        
    # Transformation, Heatmap, gating
    for data, file in zip(dataset, files):
        #Do the transformation and save plotting image
        tempdata = transformation.main(data, channel1, channel2, transformed_method, b, file, jobid)        
        tempdata = heatmapping.main(tempdata, channel1, channel2, binwidth, file, jobid)
        tempdata = gating.main(tempdata, x1, x2, y1, y2, file, jobid)
        savedir = directory.Gating(jobid) + "/" + file + ".csv"
        np.savetxt(savedir, tempdata, delimiter=",")
    try:
<<<<<<< Updated upstream
        connection = mysql.connector.connect(host='localhost',
=======
     connection = mysql.connector.connect(host='localhost',
>>>>>>> Stashed changes
                                         database='water_project',
                                         user='root',
                                         password='')
    
<<<<<<< Updated upstream
        cursor = connection.cursor()

        job_status="COMPLETED"
        cursor.execute ("""
         UPDATE jobs
         SET job1_status=%s,job2_status=%s,job3_status=%s,job4_status=%s
         WHERE job_id=%s
         """, (job_status,job_status,job_status,job_status,jobid))
    
        connection.commit()
        print(cursor.rowcount, "Record Update successfully into jobs")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
=======
     cursor = connection.cursor()

     job_status="COMPLETED"
     cursor.execute ("""
     UPDATE jobs
     SET job1_status=%s,job2_status=%s,job3_status=%s,job4_status=%s
     WHERE job_id=%s
     """, (job_status,job_status,job_status,job_status,jobid))

     connection.commit()
     print(cursor.rowcount, "Record Update successfully into jobs")
     cursor.close()

    except mysql.connector.Error as error:
     print("Failed to insert record into table {}".format(error))

    finally:
     if connection.is_connected():
        connection.close()
>>>>>>> Stashed changes
        print("MySQL connection is closed")

    return 'Fileprocess job completed'

if __name__ == '__main__':
   app.run()