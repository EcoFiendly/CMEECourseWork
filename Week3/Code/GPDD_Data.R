# Author: Yewshen Lim (y.lim20@durham.ac.uk)
# Script: GPDD_Data.R
# Created: Nov 2020
#
# Script creates a world map and superimposes it on all the locations from which
# data were provided in the GPDD dataframe

rm(list = ls())

require(maps)

# load GPDD data
load("../Data/GPDDFiltered.RData")

# draw the map
map(database = "world",
    fill = TRUE,
    col = "black",
    bg = "black",
    ylim = c(-60, 90),
    border = "white")
# plot the points
points(x = gpdd$long,
       y = gpdd$lat,
       col = "yellow",
       pch = 10,
       cex = 0.7,
       lwd = 1.1)

# Bias is reflected by the uneven distribution of data points in data, which are
# mostly located in the West Coast of North America and Europe. From past
# experience with passerine data, this distribution likely resulted from the
# developmental stage of countries, where North America and Europe had the
# resources to study these species present.