# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""Unit test for task 2F"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation,inconsistent_typical_range_stations
import floodsystem.geo
import floodsystem.analysis
import numpy as np
from datetime import datetime,timedelta
import matplotlib.pyplot as plt



def testd_polyfit():
    """Test function fitting"""
    # build a list of dates and corresponding levels
    x = np.linspace(1, 10,10)
    print([int(day) for day in x])
    t = [datetime(2023, 2, int(day)) for day in x]
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

    # Comute a least-squares fit of a polynomial of degree 4
    (poly,d0)=floodsystem.analysis.polyfit(t,y,4)

    # Plot the raw data
    plt.plot(x, y, '.')

    # Plot the function
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))

    # Display plot
    plt.show()

