# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:36:04 2021

@author: elias


# input FCS File, Output Pandas dataframe
"""
def transform_file(channel1, channel2, data, transformed_method, b):
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
    return tranformed_data
    