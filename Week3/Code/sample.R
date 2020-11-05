# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: sample.R
# Created: Oct 2020
#
# This script illustrates how lapply and sapply work and also how to
# sample random numbers

rm(list = ls())

##### Functions #####

## a function to take a sample of size n from a population "popn" and return its
## mean
myexperiment <- function(popn, n) {
    pop_sample <- sample(popn, n, replace = FALSE)
    return(mean(pop_sample))
}

## calculate means using a for loop without preallocation:
loopy_sample1 <- function(popn, n, num) {
    result1 <- vector() # initialize empty vector of size 1
    for (i in 1:num) {
        result1 <- c(result1, myexperiment(popn, n))
    }
    return(result1)
}

## to run "num" iterations of the experiment using a for loop on a vector with
## preallocation:
loopy_sample2 <- function(popn, n, num) {
    result2 <- vector(, num) # preallocate expected size
    for (i in 1:num) {
        result2[i] <- myexperiment(popn, n)
    }
    return(result2)
}

## to run "num" iterations ofthe experiment using a for loop on a list with
## preallocation:
loopy_sample3 <- function(popn, n, num) {
    result3 <- vector("list", num) # preallocate expected size
    for (i in 1:num) {
        result3[[i]] <- myexperiment(popn, n)
    }
    return(result3)
}

## to run "num" iterations of the experiment using vectorization with lapply:
lapply_sample <- function(popn, n, num) {
    result4 <- lapply(1:num, function(i) myexperiment(popn, n))
    return(result4)
}

## to run "num" iterations of the experiment using vectorization with sapply:
sapply_sample <- function(popn, n, num) {
    result5 <- sapply(1:num, function(i) myexperiment(popn, n))
    return(result5)
}

popn <- rnorm(1000) # generate the population
hist(popn)

n <- 20 # sample size for each experiment
num <- 1000 # number of times to rerun the experiment

print("The loopy, non-preallocation approach takes:")
print(system.time(loopy_sample1(popn, n, num)))

print("The loopy, but with preallocation approach takes:")
print(system.time(loopy_sample2(popn, n, num)))

print("The loopy, non-preallocation approach on a list takes:")
print(system.time(loopy_sample3(popn, n, num)))

print("The vectorized lapply apporach takes:")
print(system.time(lapply_sample(popn, n, num)))

print("The vectorized sapply approach takes:")
print(system.time(sapply_sample(popn, n, num)))