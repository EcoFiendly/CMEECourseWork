# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: apply2.R
# Created: Oct 2020
#
# SomeOperation takes an input v, if sum of v is greater than zero, it
# multiplies that value by 100. So if v has positive and negative numbers, and
# the sum comes out to be positive, only then does it multiply all the valus in
# v by 100 and return them

SomeOperation <- function(v) {
    if (sum(v) > 0) {
        return(v * 100)
    }
    return(v)
}

M <- matrix(rnorm(100), 10, 10)
print(apply(M, 1, SomeOperation))