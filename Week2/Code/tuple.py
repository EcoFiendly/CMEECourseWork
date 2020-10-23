#!/usr/bin/env python3

"""
Script to print latin name, common name and mass on separate line or output 
block by species
"""

__appname__ = '[tuple.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk'
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

def list_out(x = birds):
    """
    Uses a for loop to print latin names, common names and mass
    """
    for row in x:
        print("Latin name: " + row[0])
        print("Common name: " + row[1])
        print("Mass: " + row[2])
        print()

# Attempt list comprehension when free

def main(argv):
    """
    Prints function with argument bird
    """
    print(list_out(birds))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

