#!/usr/bin/env python3

"""
Script performs exploratory data analysis on LogisticGrowthData.csv
"""

__appname__ = '[exploration.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

# imports
import pandas as pd

# load data
df = pd.read_csv("../Data/LogisticGrowthData.csv")
# print("Loaded {} columns.".format(len(df.columns.values)))
# view column names
# print(df.columns.values)

pd.read_csv("../Data/LogisticGrowthMetaData.csv")

# df.head()

# print(df.PopBio_units.unique()) # units of the response variable
# print(df.Time_units.unique()) # units of the independent variable

# check if negative values present in Time and abs them
(df['Time'] < 0).values.any()
df['Time'] = abs(df['Time'])

# there are no ID columns, have to infer single growth curves by combining
# Species, Medium, Temp and Citation columns (each combination is unique)
df.insert(0, "ID", df.Species + "_" + df.Temp.map(str) + "_" + \
    df.Medium + "_" + df.Citation + "_" + df.Rep.map(str))

# print(df.ID.unique()) # units of the independent variable
# len(df.ID.unique())

# require minimum of 5 datapoints (1 more than number of estimates obtained)
# filter datasubsets with less than 5 datapoints
for row in df.ID.unique():
    if len(df[df['ID'] == row]) < 5:
        # print(row)
        indexNames = df[df['ID'] == row].index
        df = df.drop(indexNames)

df.numID = pd.factorize(df.ID)
df.insert(0, 'numID', df.numID[0])

df.to_csv("../Data/PreppedLGD.csv", encoding = 'utf-8')

### notes ends here ###
