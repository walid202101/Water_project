# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:49:22 2021

@author: elias
"""
# Main Directory 
foldername = 'C:/wamp64/www/frontend/public/jobs/' 

# Internal
def Rootfolder(jobid):
    return foldername + jobid
def Images(jobid):
    return Rootfolder(jobid) + "/images"

# External
def Fcs_files(jobid):
    return Rootfolder(jobid) + "/fcs_files"

def Gating(jobid):
    return Rootfolder(jobid) + "/gating"

def Differences(jobid):
    return Rootfolder(jobid) + "/differences"

def Clustering(jobid):
    return Rootfolder(jobid) + "/clustering"

def Image_transformed(jobid):
    return Images(jobid) + "/transformed"

def Image_heatmap(jobid):
    return Images(jobid) + "/heatmap"

def Image_gating(jobid):
    return Images(jobid) + "/gating"

def Image_differences(jobid):
    return Images(jobid) + "/differences"

def Image_clustering(jobid):
    return Images(jobid) + "/clustering"
