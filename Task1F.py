# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
import floodsystem.geo
import floodsystem.station


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # Build a list of all stations with inconsistent data
    inconsistentStations=floodsystem.station.inconsistent_typical_range_stations(stations)

    # Print names for stations with inconsistent data in alphabetical order
    print(sorted([station.name for station in inconsistentStations]))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
