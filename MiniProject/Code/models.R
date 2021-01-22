# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: models.R
# Created: Dec 2020
#
# This script contains the functions for the models to be used in the analysis

# temporarily setwd for ease of use
# setwd("~/CMEECourseWork/MiniProject/Code")

# function to generate range of starting values of SD = 1 around initial 
# starting values 
getStartVal <- function(ini_N0, ini_Nmax, ini_rmax, ini_tlag){
  N0 <- rnorm(100, ini_N0, 1)
  Nmax <- rnorm(100, ini_Nmax, 1)
  rmax <- rnorm(100, ini_rmax, 1)
  tlag <- rnorm(100, ini_tlag, 1)
  startVal <- data.frame(N0, Nmax, rmax, tlag)
  return(startVal)
}

##################################
# models
##################################

# logistic model
logModel <- function(N0, Nmax, rmax, t){
  # Nt = N0 * Nmax * exp(rmax * t) / (Nmax + N0 * (exp(rmax * t) - 1))
  Nt = (Nmax * N0) / (N0 + (Nmax - N0) * exp(-rmax * t))
  return(Nt)
}

# gompertz model
gomModel <- function(N0, Nmax, rmax, t, tlag){
  # Nt = A * exp(-exp((rmax * exp(1) * (tlag - t)) / A + 1))
  # Nt = N0 * (Nmax / N0) ^ (exp(-exp((exp(1) * rmax * (tlag - t)) / A + 1)))
  Nt = N0 * (Nmax / N0) ^ (exp(-exp((exp(1) * rmax * (tlag - t)) / log(Nmax / N0) + 1)))
  return(Nt)
}

# baranyi model
barModel <- function(N0, Nmax, rmax, t, tlag){
  h = rmax * tlag
  A = t + 1 / rmax * log(exp(-rmax * t) + exp(h) - exp(-rmax * t - h))
  Nt = N0 + rmax * A - log(1+(exp(rmax * A) - 1) / exp(Nmax - N0))
  return(Nt)
}