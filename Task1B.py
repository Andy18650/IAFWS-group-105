# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
import floodsystem.geo


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Use station_by distance to get a list
    distances=floodsystem.geo.stations_by_distance(stations,(52.2053,0.1218))
    
    # Print 10 closest stations
    print([(station.name,station.town,distance)
           for (station,distance) in distances[:10]])

    # Print 10 furthest stations
    print([(station.name,station.town,distance)
           for (station,distance) in distances[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
