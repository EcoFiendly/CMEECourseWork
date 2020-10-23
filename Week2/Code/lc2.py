#!/usr/bin/env python3

"""
(1) Use a list comprehension to create a list of month, rainfall tuples where
the amount of rain was greater than 100 mm.
 
(2) Use a list comprehension to create a list of just month names where the
amount of rain was less than 50 mm. 

(3) Now do (1) and (2) using conventional loops (you can choose to do 
this before 1 and 2 !). 
"""

__appname__ = '[lc2.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk'
__version__ = '0.0.1'
__license__ = ""

## Imports ##
import sys

## Constants ##

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

## Functions ##

def more_than_100_loop(x = rainfall):
    """
    Populates a list with month and rainfall tuples where the amount of rain 
    was greater than 100 mm, using a for loop and conditional
    """
    months = [] # create empty list
    for row in x: # loop through rows in x
        if row[1] > 100: # condition
            months.append(row) # if condition satistied, append row to months list
    return months

def less_than_50_loop(x = rainfall):
    """
    Populates a list with month names where the amount of rain was less than 
    50 mm, using a for loop and conditional
    """
    months = []
    for row in x:
        if row[1] < 50:
            months.append(row[0])
    return months

def more_than_100_lc(x = rainfall):
    """
    Populates a list with month and rainfall tuples where the amount of rain 
    was greater than 100 mm, using list comprehension
    """
    months = [row for row in x if row[1] > 100]
    return months

def less_than_50_lc(x = rainfall):
    """
    Populates a list with month names where the amount of rain was less than 
    50 mm, using list comprehension
    """
    months = [row[0] for row in x if row[1] < 50]
    return months

def main(argv):
    """
    Prints each of the functions with argument rainfall
    """
    print(more_than_100_loop(rainfall))
    print(less_than_50_loop(rainfall))
    print(more_than_100_lc(rainfall))
    print(less_than_50_lc(rainfall))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)