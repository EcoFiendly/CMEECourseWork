# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: boilerplate.R
# Created: Oct 2020
#
# A boilerplate R script

rm(list = ls())

MyFunction <- function(Arg1, Arg2) {

    # Statements involving Arg1, Arg2:
    # print Arg1's type
    print(paste("Argument", as.character(Arg1), "is a", class(Arg1)))
    # print Arg2's type
    print(paste("Argument", as.character(Arg2), "is a", class(Arg2)))

    return(c(Arg1, Arg2)) # this is optional, but very useful
}

MyFunction(1, 2) # test the function
MyFunction("Riki", "Tiki") # a different test