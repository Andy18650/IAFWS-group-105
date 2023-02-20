# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for task 1A"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
import floodsystem.geo


def test_stations_by_distance():
    """Test sort the stations by distance"""
    #Build a list of 2 test stations
    station_1 = MonitoringStation('station_id_t1', 'measure_id_t1', 'label_t1', (2,2), (1,1),
                 'river_t1', 'town_t1')
    station_2 = MonitoringStation('station_id_t2', 'measure_id_t2', 'label_t2', (3,3), (1,1),
                 'river_t2', 'town_t2')

    test_stations= [station_1, station_2]
    assert floodsystem.geo.stations_by_distance(test_stations, (0,0)) == [(station_1, 314.47523947196964), (station_2, 471.65293997288967)]
