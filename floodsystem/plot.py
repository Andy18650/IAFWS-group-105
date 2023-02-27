# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""This module 

"""

import matplotlib.pyplot as plt
from datetime import datetime

def plot_water_levels(station, dates, levels):

    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station "+station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_levels_list(station, dates, levels):
    # Plot
    plt.plot(dates, levels)
    plt.plot(dates, [level+0.1 for level in levels])

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station "+station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
