# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""This module 

"""

from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    """ This fucntion returns a list of stations with relative level higher
        than tol, sorted by relative level """
    return sorted_by_key([(station,station.relative_water_level()) for station in stations if station.relative_water_level() != None and station.relative_water_level() > tol],1)[::-1]

def stations_highest_rel_level(stations, N):
    """ This function returns a list of N stations with highest relative level """
    sortedStationLevel = sorted_by_key([(station,station.relative_water_level()) for station in stations if station.relative_water_level() != None],1)[:-N-1:-1]
    return [station for (station,level) in sortedStationLevel]
