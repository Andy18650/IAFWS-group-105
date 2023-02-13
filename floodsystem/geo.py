# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """ This function returns a list of (station,distance) tuples
        sorted by distance """
    return sorted_by_key([(station,haversine(station.coord,p))
                          for station in stations],1)

def stations_within_radius(stations, centre, r):
    """ This function returns a list of all stations within radius r
        of geographics coordinate defined by centre"""
    stationWithinRadius=[]
    for station in stations:
        if haversine(station.coord,centre) <= r:
            stationWithinRadius.append(station)
    return stationWithinRadius
