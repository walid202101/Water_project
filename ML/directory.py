# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:49:22 2021

@author: elias
"""
# Main Directory
foldername = r'C:\Users\elias\Documents\GitHub\Water_project\ML\Jobs\1'
     

def fcsfilesfolder(jobid):
    return foldername + "/fcsfiles" 

def gatingfolder(jobid):
    return foldername + "/gating"

def difffolder(jobid):
    return foldername + "/differences" 

def imageolder(jobid):
    return foldername + "/images" 

def clusteringfolder(jobid):
    return foldername + "/clustering" 