# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    distances=[]
    for station in stations:
        distance=haversine(station.coord,p)
        distances.append((station,distance))
    return sorted_by_key(distances,1)
