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
    return [station for station in stations if haversine(station.coord,centre) <= r]

def rivers_by_station_number(stations, N):
    """ This function returns a list of N rivers with the greatest
        number of monitoring stations"""
    rivers={}
    for station in stations:
        if station.river in rivers:
            rivers[station.river]+=1
        else:
            rivers[station.river]=1
    sortedRivers=sorted_by_key([(river,rivers[river]) for river in rivers],1)
    riversByStationNumber=sortedRivers[-1:-N-1:-1]
    for i in range(N,len(sortedRivers)):
        if sortedRivers[-i-1][1] == sortedRivers[-i][1]:
            riversByStationNumber.append(sortedRivers[-i-1])
        else:
            break
    return riversByStationNumber

def rivers_with_station(stations):
    return {station.river for station in stations}

def stations_by_river(stations):
    return {riverName : [station for station in stations if station.river == riverName] for riverName in rivers_with_station(stations)}
