# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""Unit test for task 2C"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation,inconsistent_typical_range_stations
import floodsystem.geo, floodsystem.flood


def test_stations_highest_rel_level():
    """Test get list of station with highest relative level"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Test get 10 stations with highest relative water level
    riskStations=floodsystem.flood.stations_highest_rel_level(stations, 10)
    assert len(riskStations)==10

    # Test if the list is sorted in descending order
    for i in range(len(riskStations)-1):
        assert riskStations[i].relative_water_level() > riskStations[i+1].relative_water_level()

    
