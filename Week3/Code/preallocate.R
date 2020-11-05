# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: preallocate.R
# Created: Oct 2020
#
# Script illustrates how preallocation speeds up a loop that resizes a vector
# repeatedly

rm(list = ls())

a <- NA
nopreallo <- function(a) {
    for (i in 1:10000) {
        a <- c(a, i)
        # print(a)
        # print(object.size(a))
    }
}

print("Without preallocation, time taken is:")
print(system.time(nopreallo(a)))

a <- rep(NA, 10000)
preallo <- function(a) {
    for (i in 1:10000) {
        a[i] <- i
        # print(a)
        # print(object.size(a))
    }
}

print("With preallocation, time taken is:")
print(system.time(preallo(a)))