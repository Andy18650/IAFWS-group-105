# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""Unit test for task 2C"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation,inconsistent_typical_range_stations
import floodsystem.geo, floodsystem.flood
from datetime import datetime
import floodsystem.plot


def test_plot_water_levels():
    """Test plot water leevels for a station"""
    
    # Build a test station
    station=MonitoringStation('station_id_t1', 'measure_id_t1', 'label_t1', (2,2), (1,1),
                 'river_t1', 'town_t1')

    # Build a list of dates and corresponding water levels
    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
    level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    floodsystem.plot.plot_water_levels(station,t,level)
