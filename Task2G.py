# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood
import floodsystem.plot
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def run():
    """Requirements for Task 2G"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    severe_stations=[]
    high_stations=[]
    moderate_stations=[]
    low_stations=[]

    for station in stations:
        if station.relative_water_level()==None:
            #print(station.name)
            continue
        elif station.relative_water_level() > 1:
            severe_stations.append(station)
        elif station.relative_water_level() > .5:
            moderate_stations.append(station)
        else:
            low_stations.append(station)
    for severe_station in severe_stations:
        print(severe_station.name,severe_station.relative_water_level(),severe_station.town)
        
    


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
