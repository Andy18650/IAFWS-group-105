# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""Unit test for task 1F"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation,inconsistent_typical_range_stations
import floodsystem.geo


def test_consistent_typial_range_stations():
    """Test for consistent typical range stations"""
    # build a list of many test stations
    stations = build_station_list()
    inconsistent_stations = [x.name for x in inconsistent_typical_range_stations(stations)]
    assert 'Apperly Bridge' not in inconsistent_stations

def test_inconsistent_typical_range_stations():
    """Test for inconsistent typical range stations"""
    # build a list of many test stations
    stations = build_station_list()
    inconsistent_stations = [x.name for x in inconsistent_typical_range_stations(stations)]
    assert 'Airmyn' in inconsistent_stations

def test_typical_range_consistent():
    """Test check data consistency"""
    # build two test stations, one consistent, one inconsistent
    station_1 = MonitoringStation('station_id_t1', 'measure_id_t1', 'label_t1', (2,2), (1,2),
                 'river_t1', 'town_t1')
    station_2 = MonitoringStation('station_id_t2', 'measure_id_t2', 'label_t2', (3,3), (2,1),
                 'river_t2', 'town_t2')

    assert station_1.typical_range_consistent() == True
    assert station_2.typical_range_consistent() == False
