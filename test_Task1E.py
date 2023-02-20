# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""Unit test for task 1E"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import floodsystem.geo


def test_river_by_station_number():
    """ Checks that a list of tuples is returned.
    Checks the length of output (output can be greater of equal to N if there
    are more rivers with the same number of stations as the Nth entry) """


    #Build a list of many test stations
    
    stations = build_station_list()
    assert type (floodsystem.geo.rivers_by_station_number(stations,10)[0]) == tuple
    assert len(floodsystem.geo.rivers_by_station_number(stations,10)) >= 10
