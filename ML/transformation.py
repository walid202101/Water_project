# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:36:04 2021

@author: elias


# input FCS File, Output Pandas dataframe
"""
from FlowCytometryTools import FCMeasurement
from pylab import plt

import mysql.connector
import directory
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/transformation')  

def main():
    
    inputfile = directory.fcsfiles_path(request.args.get('inputfile'))
    outputfile = directory.transform_path(request.args.get('outputfile'))
    channel1=request.args.get('channel1')
    channel2=request.args.get('channel2')
    transformed_method = request.args.get('transformed_method')
    b = int(request.args.get('b'))
    
    #Read & Transform
    data = FCMeasurement(ID=inputfile, datafile=inputfile)
    # Transformations
    # The presence of both very dim and very bright cell populations in flow cytometry data can make
    # it difficult to simultaneously visualize both populations on the same plot. To address this problem,
    # flow cytometry analysis programs typically apply a transformation to the data to make it easy to visualize and
    # interpret properly. Rather than having this transformation applied automatically and without your knowledge,
    # this package provides a few of the common transformations (e.g., hlog, tlog), but ultimately leaves it up to you
    # to decide how to manipulate your data.
    data = data.transform(
        transformed_method,
        channels=[channel1, channel2],
        b=b)
    
    tranformed_data = data.data[[channel1, channel2]]
    tranformed_data.to_csv(outputfile + ".csv")
    
    # Plotting
    x = data[channel1]
    y = data[channel2]
    plt.figure()
    plt.xlabel(channel1)
    plt.ylabel(channel2)
    plt.scatter(x, y, facecolors = 'blue', edgecolors='none', s=0.25)
    plt.savefig(outputfile + ".png")
    plt.show()
    return 'Done'
    
if __name__ == '__main__':
   app.run()