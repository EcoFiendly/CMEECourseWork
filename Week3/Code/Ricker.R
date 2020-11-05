# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: Ricker.R
# Created: Oct 2020
#
# This script runs a simulation of the Ricker model and returns a vector of
# length generations
#
# ARGUMENTS:
# N0 = initial density of population
# r = intrinsic growth rate
# K = carrying capacity of the environment
#
# OUTPUT
# density of population after a number of generations

rm(list = ls())

Ricker <- function(N0 = 1, r = 1, K = 10, generations = 50) {
    N <- rep(NA, generations) # creates a vector of NA

    N[1] <- N0
    for (t in 2:generations) {
        N[t] <- N[t - 1] * exp(r * (1.0 - (N[t - 1] / K)))
    }
    return(N)
}

plot(Ricker(generations = 10), type = "l")