# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: control_flow.R
# Created: Oct 2020
#
# Script illustrates the use of control flow in R

rm(list = ls())

## if statements ##

a <- TRUE
if (a == TRUE) {
    print("a is TRUE")
    } else {
    print("a is FALSE")
    }

# writing an if statement in one line
z <- runif(1) ## Generate a uniformly distributed random number
if (z <= 0.5) {
    print("Less than a half")
    }

# code readability is important, so avoid squeezing control flow blocks into a
# single line

## for loops ##

for (i in 1:10) {
    j <- i * i
    print(paste(i, " squared is", j))
}

# loop over a vector of strings
for (species in c("Heliodoxa rubinoides",
                 "Boissonneaua jardini",
                 "Sula nebouxii")) {
    print(paste("The species is", species))
}

# for loop using a pre-existing vector
v1 <- c("a", "bc", "def")
for (i in v1) {
    print(i)
}

## while loops ##

i <- 0
while (i < 10) {
    i <- i + 1
    print(i ^ 2)
}