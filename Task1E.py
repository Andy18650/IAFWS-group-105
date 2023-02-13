# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
import floodsystem.geo


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Print 9 rivers with most monitoring stations
    print(floodsystem.geo.rivers_by_station_number(stations,9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
