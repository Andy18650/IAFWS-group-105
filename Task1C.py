# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
import floodsystem.geo


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Build a list of stations within 10km from Cambridge
    stationsCambridge=floodsystem.geo.stations_within_radius(stations,(52.2053,0.1218),10)

    # Print the name of the selected stations
    print([station.name for station in stationsCambridge])


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
