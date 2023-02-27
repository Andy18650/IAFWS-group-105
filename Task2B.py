# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood

def run():
    """Requirements for Task 2B"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print stations with relative level over 0.8
    for (station,level) in floodsystem.flood.stations_level_over_threshold(stations, 0.8):
        print(station.name,level)
    


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
