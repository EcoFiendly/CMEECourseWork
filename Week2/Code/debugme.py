#!/usr/bin/env python3

"""
Example of debugging on a script
"""

__appname__ = '[debugme.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = ""

## Functions ##

def buggyfunc(x):
    """
    Buggy function for debugging
    """
    y = x
    for i in range(x):
        y = y-1
        z = x/y
    return z

buggyfunc(20)