#!/usr/bin/env python3

"""
Basic control flow. 
Modification to original cfexercises1.py to turn it into a module like
control_flow.py
Also added test arguments to show that they work
"""

__appname__ = '[cfexercises1.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = ""

## Imports ##
import sys # module to interface our program with the OS

## Constants ##

## Functions ##

# What does each of foo_x do?
def foo_1(x=4):
    """
    Multiply x by 0.5 / square root x
    """
    return x ** 0.5
 
def foo_2(x=5, y=10):
    """
    Returns x if x > y, else return y
    """
    if x > y:
        return x
    return y

def foo_3(x=10, y=7, z=4):
    """
    Rearranges x, y, z in ascending order
    """
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo_4(x=5):
    """
    Returns factorial of x
    """
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo_5(x=6): 
    """
    A recursive function that calculates the factorial of x
    """
    if x == 1:
        return 1
    return x * foo_5(x-1)

def foo_6(x=4):
    """
    Calculate the factorial of x in a different way
    """
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

def main(argv):
    """
    Prints each of the function with arguments provided
    """
    print(foo_1(25))
    print(foo_2(20, 25))
    print(foo_3(2, 20, 15))
    print(foo_4(7))
    print(foo_5(7))
    print(foo_6(7))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)