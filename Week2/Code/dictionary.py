#!/usr/bin/env python3

"""
Script populates a dictionary called taxa_dic derived from taxa so that it maps 
order names to set of taxa.
"""

__appname__ = '[dictionary.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk'
__version__ = '0.0.1'
__license__ = ""

## Imports ##
import sys

## Constants ##

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

## Functions ##

def make_di(x=taxa):
        """
        Makes a dictionary
        """
        di = {}
        for i, j in x:
                di[j] = di.get(j, ()) + (i,)
        return di

def main(argv):
        """
        Makes a dictionary from taxa, a list
        """
        print(make_di(taxa))
        return 0

if (__name__ == "__main__"):
        status = main(sys.argv)
        sys.exit(status)