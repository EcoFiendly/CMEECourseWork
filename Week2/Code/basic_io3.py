#!/usr/bin/env python3

"""
Script illustates basic storage of objects
"""

__appname__ = '[basic_io3.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

#################################
# STORING OBJECTS 
#################################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle
f = open('../Sandbox/testp.p', 'wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
f = open('../Sandbox/testp.p', 'rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)