# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: break.R
# Created: Oct 2020
#
# Script illustrates how to break out of a loop

rm(list = ls())

## breaking out of a loop ##

i <- 0 #Initialize i
    while (i < Inf) {
        if (i == 10) {
            break # break out of the while loop!
            }
        else {
            cat("i equals ", i, " \n")
            i <- i + 1 # update i
   }
}