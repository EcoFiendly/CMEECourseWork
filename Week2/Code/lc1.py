#!/usr/bin/env python3

"""
(1) Write three separate list comprehensions that create three different
lists containing the latin names, common names and mean body masses for
each species in birds, respectively. 

(2) Now do the same using conventional loops (you can choose to do this 
before 1 !). 
"""

__appname__ = '[lc1.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = ""

## Imports ##
import sys

## Constants ##

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

## Functions ##

def latin_names_loop(x = birds):
    """
    Populates a list with latin names using a for loop
    """
    latin_names = []
    for row in x:
        latin_names.append(row[0])
    return latin_names

def common_names_loop(x = birds):
    """
    Populates a list with common names using a for loop
    """
    common_names = []
    for row in x:
        common_names.append(row[1])
    return common_names

def masses_loop(x = birds):
    """
    Populates a list with masses using a for loop
    """
    masses = []
    for row in x:
        masses.append(row[2])
    return masses

def latin_names_lc(x = birds):
    """
    Populates a list with latin names using list comprehension
    """
    latin_names = [row[0] for row in x]
    return latin_names

def common_names_lc(x = birds):
    """
    Populates a list with common names using list comprehension
    """
    common_names = [row[1] for row in x]
    return common_names

def masses_lc(x = birds):
    """
    Populates a list with masses using list comprehension
    """
    masses = [row[2] for row in x]
    return masses

def main(argv):
    """
    Prints each of the functions with argument birds
    """
    print(latin_names_loop(birds))
    print(common_names_loop(birds))
    print(masses_loop(birds))
    print(latin_names_lc(birds))
    print(common_names_lc(birds))
    print(masses_lc(birds))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)