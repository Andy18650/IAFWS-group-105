# Copyright (C) 2023 Jiajun Hu
#
# SPDX-License-Identifier: MIT
"""This module 

"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit([t-x[0] for t in x], levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return (poly,dates[0])
