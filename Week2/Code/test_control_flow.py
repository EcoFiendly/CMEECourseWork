#!/usr/bin/env python3

"""
Some functions exemplifying the use of control statements
"""

__appname__ = '[test_control_flow.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## Imports ##
import sys # module to interface our program with the operating system
import doctest # import the doctest module

## Constants ##


## Functions ##
def even_or_odd(x=0): # if not specified, x should take value 0
    """
    Find whether a number x is even or odd.

    >>> even_or_odd(10)
    '10 is Even!'

    >>> even_or_odd(5)
    '5 is Odd!'

    whenever a float is provided, then the closest integer is used:
    >>> even_or_odd(3.2)
    '3 is Odd!'

    in case of negative numbers, the positive is taken:
    >>> even_or_odd(-2)
    '-2 is Even!'

    """
    # Define function to be tested
    if x % 2 == 0: # the conditional if
        return "%d is Even!" % x
    return "%d is Odd!" % x

def main(argv):
    """
    Prints each of the function with given argument
    """
    print(even_or_odd(22))
    print(even_or_odd(33))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    # sys.exit(status)
# Can suppress the block of code containing def main() and if 
# (__name__ == "__main__") because you don't want/need to unit test that section
# of the output

doctest.testmod() # To run with embedded tests