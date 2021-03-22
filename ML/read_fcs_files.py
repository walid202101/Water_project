# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:31:31 2021

@author: elias
"""
import os
import pandas as pd
import numpy as np
from FlowCytometryTools import FCMeasurement

def loading_fcs_from_directory(directory):
    datasets = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".fcs") | file.endswith('.FCS'):
                sample = FCMeasurement(ID=file, datafile=(directory + "/" + file))
                datasets.append(sample)
    return datasets

def channels_name(data):
    # Channel Information to know which channels were measured
    return data.channel_names


def meta_data(data):
    # Full Meta Data
    # The FCS files contain “meta” information about the measurements, which may be useful for data analysis.
    # You can access this information using the meta property, which will return a python dictionary.
    # The meaning of the fields in meta data is explained in the FCS format specifications
    # (google for the specification)
    return data.meta

def save_dataframe(data, _dir, _filename):
    pd.DataFrame.to_csv(_dir + "/" + _filename + ".csv")
    
def load_dataframe(_dir, _filename):
    return pd.read_csv(_dir + "/" + _filename + ".csv")
    
    
def save_array(data, _dir, _filename):
    path = _dir  + "/" + _filename + ".csv"
    np.savetxt(path, data, delimiter=",")
    
def load_array(_dir, _filename):
    np.genfromtxt(_dir + "/" + _filename + ".csv",delimiter=',')
    

    
