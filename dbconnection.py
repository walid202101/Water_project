# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:30:01 2021

@author: elias
"""
import mysql.connector

def main(jobid, jobstatusnum):
    try:
        connection = mysql.connector.connect(host='localhost', database='water_project', user='root', password='2020@Jambot',auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        job_status="COMPLETED"
        
        if(jobstatusnum ==1):
            cursor.execute ("""UPDATE jobs SET job1_status=%s,job2_status=%s,job3_status=%s,job4_status=%s WHERE job_id=%s    """, (job_status,job_status,job_status,job_status,jobid))
        elif(jobstatusnum==2):
            cursor.execute ("""UPDATE jobs SET job5_status=%s WHERE job_id=%s""", (job_status,jobid))
        elif(jobstatusnum==3):
            cursor.execute ("""UPDATE jobs SET job6_status=%s WHERE job_id=%s""", (job_status,jobid))
        
        connection.commit()
        print(cursor.rowcount, "Record Update successfully into jobs")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into table {}".format(error))
    finally:
     if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

    if(jobstatusnum ==1):
        return 'Fileprocess job completed'    
    elif(jobstatusnum==2):
        return 'difference and reducing job completed'    
    elif(jobstatusnum==3):
        return 'clustering job completed'   
    
    
    