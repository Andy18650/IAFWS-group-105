# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
import floodsystem.geo


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Find rivers with one or more monitoring station(s)
    riversWithStation=list(floodsystem.geo.rivers_with_station(stations))
    riversWithStation.sort()

    # Print the number of rivers with station(s) and a list of the first 10
    print(len(riversWithStation),'stations. First 10 -',riversWithStation[:10])
    # I think this output is a bit confusing since it says 'x stations',
    # but it should be 'x rivers' or 'x rivers with station(s)'

    # Get the dictionary that maps rivers to a list of stations
    stationByRiver=floodsystem.geo.stations_by_river(stations)

    # Print the names of stations on required rivers in alphabetical order
    for river in [
        'River Aire','River Cam','River Thames'
        ]:
        stationList=[station.name for station in stationByRiver[river]]
        print(sorted(stationList))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
