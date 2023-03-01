# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""Unit test for task 2B"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation,inconsistent_typical_range_stations
import floodsystem.geo, floodsystem.flood


def test_stations_level_over_threshold():
    """Test get list of station data over threshold"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Test stations with relative level over 0.8
    for (station,level) in floodsystem.flood.stations_level_over_threshold(stations, 0.8):
        assert level > 0.8

    
