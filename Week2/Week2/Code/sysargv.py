#!/usr/bin/env python3

"""
argv is the 'argument variable'. Such variables are necessarily very common
across programming languages, and play an important role - argv is a variable 
that holds the arguments passed to the script when it's ran.
"""

__appname__ = '[sysargv.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk'
__version__ = '0.0.1'
__license__ = ""

## Imports ##
import sys

## Functions ##
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("othe arguments are: " , str(sys.argv))
