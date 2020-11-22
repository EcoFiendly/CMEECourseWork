#!/usr/bin/env python3

"""
Script illustrates the use of cProfile to profile LV1.py, LV2.py and LV3.py
Prints first 50 rows sorted by total time for each profile
"""

__appname__ = '[run_LV.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

# imports
import cProfile
import pstats
import LV1
import LV2
import LV3

# list of LV to profile
listLV = [LV1, LV2, LV3]
# loop profiling
for i in listLV:
    # create a profile
    profStats = cProfile.Profile()
    # enable profile
    profStats.enable()
    # run main function for each item in list
    i.main()
    # disable profile
    profStats.disable()
    # print 50 rows, sorted by total time
    ps = pstats.Stats(profStats).sort_stats("tottime").print_stats(50)