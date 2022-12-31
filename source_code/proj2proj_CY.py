"""
:copyright: 2019 Geophysics Labs
:author: Joseph Barraud
:license: BSD License
"""
# import system modules
import os
import argparse
import re
import decimal

# import numpy
import numpy as np

# import local modules
from spatial import projectPoints
# ==============================================================================
# segy2segy
# ==============================================================================


def segy2segy(s_srs, t_srs, X, Y):
    '''
    Both of X and Y are list type.
    convert one XY projection to other one XY projection only
    '''
    XYarray = np.zeros((len(X), 2), dtype=np.float)

    XYarray[:, 0] = X
    XYarray[:, 1] = Y

    # transform coordinates
    return_dict = {}
    newXYarray = projectPoints(XYarray, s_srs, t_srs)

    print("------>")
    # print(newXYarray)
    print("------>")

    new_lat_list =[]
    new_lon_list =[]
    for latlon_set in newXYarray:
        new_lat_list.append(str(latlon_set[0]))

    for latlon_set in newXYarray:
        new_lon_list.append(str(latlon_set[1]))

    # return_dict['lat'] = str(newXYarray[:, 0])
    # return_dict['lon'] = str(newXYarray[:, 1])

    return_dict['lat'] = new_lat_list
    return_dict['lon'] = new_lon_list

    return return_dict
