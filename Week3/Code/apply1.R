# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: apply1.R
# Created: Oct 2020
#
# This script applies the same function to rows/columns of a matrix

## Build a random matrix
M <- matrix(rnorm(100), 10, 10)

## Take the mean of each row
RowMeans <- apply(M, 1, mean)
print(RowMeans)

## Now the variance
RowVars <- apply(M, 1, var)
print(RowVars)

## By column
ColMeans <- apply(M, 2, mean)
print(ColMeans)

ColVars <- apply(M, 2, var)
print(ColVars)