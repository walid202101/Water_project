
"""
Created on Fri Feb 19 08:21:17 2021
@author: elias
"""


import os

import numpy as np
from pylab import plt
from FlowCytometryTools import FCMeasurement, FCPlate
from matplotlib import cm


class Utils:
    def __init__(self):
        pass


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
    return data.channels_name


def meta_data(data):
    # Full Meta Data
    # The FCS files contain “meta” information about the measurements, which may be useful for data analysis.
    # You can access this information using the meta property, which will return a python dictionary.
    # The meaning of the fields in meta data is explained in the FCS format specifications
    # (google for the specification)
    return data.meta


def plot_fl1_fl3(data, title):
    x_label = 'FL1-A'
    y_label = 'FL3-A'
    x = data[x_label]
    y = data[y_label]
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    extent = [0, 10000, 0, 10000]
    plt.clf()
    plt.xlim(0,10000)
    plt.ylim(0,10000)
    plt.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
    plt.xlabel(x_label)
    plt.ylabel(y_label)     
    plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='hot')
    plt.title(title, fontsize=8)
    plt.show()
    
    
def plot_sca_fca(data, title):
    x_label = 'SSC-A'
    y_label = 'FSC-A'
    x = data[x_label]
    y = data[y_label]
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    extent = [0, 10000, 0, 10000]
    """
    plt.clf()
    plt.xlim(0,10000)
    plt.ylim(0,10000)
    plt.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
    plt.xlabel(x_label)
    plt.ylabel(y_label)     
    plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='hot')
    plt.title(title, fontsize=8)
    plt.show()
    """
    plt.scatter(x, y, color='r', s=0.5)
    plt.show()

def clean_data(df):
    df = df[(df['SSC-A'] >= 10.0) & (df['FSC-A'] >= 10.0)]
    return df

def plate(data1, data2):
    # Group in plate
    plate = FCPlate('demo plate', [data1, data2], 'name')
    plate = plate.dropna()
    return plate


def transformed_data(data):
    # Transformations
    # The presence of both very dim and very bright cell populations in flow cytometry data can make
    # it difficult to simultaneously visualize both populations on the same plot. To address this problem,
    # flow cytometry analysis programs typically apply a transformation to the data to make it easy to visualize and
    # interpret properly. Rather than having this transformation applied automatically and without your knowledge,
    # this package provides a few of the common transformations (e.g., hlog, tlog), but ultimately leaves it up to you
    # to decide how to manipulate your data.
    data = data.transform(
        'hlog',
        channels=['FSC-A', 'SSC-A', 'FL1-A', 'FL2-A', 'FL3-A', 'FL4-A', 'FSC-H', 'SSC-H', 'FL1-H', 'FL2-H', 'FL3-H', 'FL4-H', 'Width', 'Time'],
        b=50.0)
    return data

