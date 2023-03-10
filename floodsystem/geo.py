# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

There is no exception in this library!

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
    return [station for station in stations
            if haversine(station.coord,centre) <= r]

def rivers_with_station(stations):
    """ This function returns a set of all rivers with one or more
        station(s) on it"""
    return {station.river for station in stations}

def stations_by_river(stations):
    """ This function returns a dictionary that maps river name to
        a list of all stations on it"""
    return {riverName :
            [station for station in stations if station.river == riverName]
            for riverName in rivers_with_station(stations)}

def rivers_by_station_number(stations, N):
    """ This function returns a list of N rivers with the greatest
        number of monitoring stations"""
    return [magicTuple[1] for magicTuple in
            zip(range(1,len(stations_by_river(stations))+1),
                sorted_by_key([(river,len(stationList)) for (river,stationList)
                               in list(stations_by_river(stations).items())],1)
                [::-1],
                [sorted_by_key([(river,len(stationList)) for (river,stationList)
                                in list(stations_by_river(stations).items())],1)
                 [-N][1]]*len(stations_by_river(stations)))
            if magicTuple[0] <= N or magicTuple[1][1] == magicTuple[2]]
