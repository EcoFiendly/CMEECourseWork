#!/usr/bin/env python3

"""
Script illustrates basic output
"""

__appname__ = '[basic_io2.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

#################################
# FILE OUPUT
#################################
# Save the elements of a list to a file
list_to_save = range(100)

f = open('../Sandbox/testout.txt', 'w')
for i in list_to_save:
    f.write(str(i) + '\n')  ## oadd a new line at the end

f.close()