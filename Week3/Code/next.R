# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: next.R
# Created: Oct 2020
#
# Script illustrates the use of next

rm(list = ls())

## next ##

for (i in 1:10) {
    if ((i %% 2) == 0) # check if the number is odd
        next # pass to next iteration of loop
    print(i)
}