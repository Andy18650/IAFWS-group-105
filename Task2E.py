# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood
import floodsystem.plot
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def run():
    """Requirements for Task 2E"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for station in floodsystem.flood.stations_highest_rel_level(stations, 5):
        (dates, levels) = floodsystem.datafetcher.fetch_measure_levels(station.measure_id, timedelta(10))
        floodsystem.plot.plot_water_levels(station,dates,levels)
    


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
