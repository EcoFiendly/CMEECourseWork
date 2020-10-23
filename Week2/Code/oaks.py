#!/usr/bin/env python3

"""
Finds just taxa that aro oak trees from a list of species using both loops and
list comprehension
"""

__appname__ = '[oaks.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

taxa = [ 'Quercus robur',
         'Fraxinus excelsior',
         'Pinus sylvestris',
         'Quercus cerris',
         'Quercus petraea',
       ]

def is_an_oak(name):
    """
    Returns True if name starts with 'quercus'
    """
    return name.lower().startswith('quercus ')

## Using for loops
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species)
print(oaks_loops)

## Using list comprehensions
oaks_lc = set([species for species in taxa if is_an_oak(species)])
print(oaks_lc)

## Get names in UPPER CASE using for loops
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species.upper())
print(oaks_loops)

## Get names in UPPER CASE using list comprehensions
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)])
print(oaks_lc)
