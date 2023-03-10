# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""Unit test for task 1C"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
import floodsystem.geo


def test_stations_within_radius():
    """Test get station within radius"""
    #Build a list of 2 test stations
    station_1 = MonitoringStation('station_id_t1', 'measure_id_t1', 'label_t1', (2,2), (1,1),
                 'river_t1', 'town_t1')
    station_2 = MonitoringStation('station_id_t2', 'measure_id_t2', 'label_t2', (3,3), (1,1),
                 'river_t2', 'town_t2')

    test_stations= [station_1, station_2]
    assert floodsystem.geo.stations_within_radius(test_stations, (0,0), 320) == [station_1]
