# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood

def run():
    """Requirements for Task 2C"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print 10 stations at which the current relative level is highest
    for station in floodsystem.flood.stations_highest_rel_level(stations, 10):
        print(station.name,station.relative_water_level())
    


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
