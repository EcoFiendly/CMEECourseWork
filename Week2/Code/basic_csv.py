#!/usr/bin/env python3

"""
Script illustrates the manipulation of csv files
"""

__appname__ = '[basic_csv.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

import csv
# Read a file containing:
# 'Species', 'Infraorder', 'Family', 'Distribution', 'Body mass male (Kg)'
f = open('../Data/testcsv.csv', 'r')

csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
    print(row)
    print("the species is", row[0])

f.close()

# Write a file containing only species name and Body mass
f = open('../Data/testcsv.csv', 'r')
g = open('../Data/bodymass.csv', 'w')

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
    print(row)
    csvwrite.writerow([row[0], row[4]])

f.close()
g.close()