#!/usr/bin/env python3

"""
Description of this program or application.
You can use several lines
"""

__appname__ = '[boilerplate.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## Imports ##
import sys # module to interface our program with the operating system

## Constants ##


## Functions ##
def main(argv):
    """
    Main entry point of the program
    """
    print('This is a boilerplate') # Note: indented using two tabs or 4 spaces
    return 0

if __name__ == "__main__":
    """
    Makes sure the "main" function is called from command line
    """
    status = main(sys.argv)
    sys.exit(status)