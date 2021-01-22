# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: modelapply.R
# Created: Dec 2020
#
# This script applies the models to the cleaned dataframe to identify the best
# fits and records the parameters.

# temporarily setwd for ease of use
# setwd("~/CMEECourseWork/MiniProject/Code")

rm(list=ls())

# packages
library("minpack.lm")
library("tidyverse")
source("models.R")

# set seed for reproducibility
set.seed(95)

# load prepped data
df <- read.csv("../Data/PreppedLGD.csv")
subsetID <- unique(df$numID)

# check number of units
# nrow(subset(df, PopBio_units == "OD_595")) # 1878
# nrow(subset(df, PopBio_units == "N")) # 1260
# nrow(subset(df, PopBio_units == "CFU")) # 1171
# nrow(subset(df, PopBio_units == "DryWeight")) # 54

# initialize empty dataframe to store fit statistics for each unique ID
fitStats = data.frame(Species = character(),
                      ID = character(),
                      Temp = character(),
                      Medium = character(),
                      polyAIC = numeric(),
                      polyBIC = numeric(),
                      logiAIC = numeric(),
                      logiBIC = numeric(),
                      gomAIC = numeric(),
                      gomBIC = numeric(),
                      barAIC = numeric(),
                      barBIC = numeric(),
                      stringsAsFactors = FALSE)

# initialize empty dataframe to store fit parameters for each unique ID
fitPara = data.frame(ID = character(),
                     a = character(),
                     b = character(),
                     c = character(),
                     d = character(),
                     logiN0 = character(),
                     logiNmax = character(),
                     logiRmax = character(),
                     gomN0 = character(),
                     gomNmax = character(),
                     gomRmax = character(),
                     gomTlag = character(),
                     barN0 = character(),
                     barNmax = character(),
                     barRmax = character(),
                     barTlag = character())

# loop through every data subset
for (i in 1:length(subsetID)){
  # subset ID
  dfSubset <- df[which(df$numID == subsetID[i]),]
  dfSubset$PopBio <- log10(dfSubset$PopBio)
  # N0 and Nmax
  ini_N0 <- min(dfSubset$PopBio)
  ini_Nmax <- max(dfSubset$PopBio)

  # rmax
  j <- which.max(diff(dfSubset$PopBio))
  ini_rmax <- max(diff(dfSubset$PopBio))/(dfSubset[j+1,"Time"]-dfSubset[j,"Time"])
  # tlag
  ini_tlag <- dfSubset$Time[which.max(diff(diff(dfSubset$PopBio)))]
  
  # get starting values
  startVal <- getStartVal(ini_N0, ini_Nmax, ini_rmax, ini_tlag)
  
  # store fitted stats
  polyStats <- data.frame(polyAIC = numeric(),
                          polyBIC = numeric(),
                          polya = numeric(),
                          polyb = numeric(),
                          polyc = numeric(),
                          polyd = numeric())
  logiStats <- data.frame(logiAIC = numeric(),
                          logiBIC = numeric(), 
                          logiN0 = numeric(),
                          logiNmax = numeric(),
                          logiRmax = numeric())
  gomStats <- data.frame(gomAIC = numeric(),
                          gomBIC = numeric(),
                          gomN0 = numeric(),
                          gomNmax = numeric(),
                          gomRmax = numeric(),
                          gomTlag = numeric())
  barStats <- data.frame(barAIC = numeric(),
                          barBIC = numeric(),
                          barN0 = numeric(),
                          barNmax = numeric(),
                          barRmax = numeric(),
                          barTlag = numeric())
  
  
  #############################################################
  # model fitting
  #############################################################
  # cubic fit
  polyFit <- try(lm(dfSubset$PopBio ~ poly(dfSubset$Time, 3, raw = TRUE)), silent = TRUE)
  
  # check for successful fits
  if (class(polyFit) != "try-error"){
    polyStats[i,] <- c(AIC(polyFit),
                      BIC(polyFit),
                      coef(polyFit)[4],
                      coef(polyFit)[3],
                      coef(polyFit)[2],
                      coef(polyFit)[1])
  } else {
    polyStats[i,] <- rep(NA, 6)
  }
  
  for (row in 1:nrow(startVal)){
    # logistic fit
    logiFit <- try(nlsLM(PopBio ~ logModel(N0, Nmax, rmax, t = dfSubset$Time),
                         dfSubset, start = list(N0 = startVal[row,1],
                                           Nmax = startVal[row,2],
                                           rmax = startVal[row,3]),
                         lower = c(startVal[row,1]-abs(2*startVal[row,1]),
                                   startVal[row,2]-abs(2*startVal[row,2]),
                                   startVal[row,3]-abs(1.5*startVal[row,3])),
                         upper = c(startVal[row,1]+abs(2*startVal[row,1]),
                                   startVal[row,2]+abs(2*startVal[row,2]),
                                   startVal[row,3]+abs(1.5*startVal[row,3])),
                         control = nls.lm.control(maxiter = 400)),
                   silent = TRUE)
  
    if (class(logiFit) != "try-error"){
      logiStats[row,] <- c(AIC(logiFit),
                          BIC(logiFit),
                          coef(logiFit)['N0'],
                          coef(logiFit)['Nmax'],
                          coef(logiFit)['rmax'])
    } else {
      logiStats[row,] <- c(rep(NA, 5))
    }
    
    # gompertz fit
    gomFit <- try(nlsLM(PopBio ~ gomModel(N0, Nmax, rmax, t = dfSubset$Time, tlag),
                        dfSubset, list(N0 = startVal[row,1],
                                       Nmax = startVal[row,2],
                                       rmax = startVal[row,3],
                                       tlag = startVal[row,4]),
                        lower = c(startVal[row,1]-abs(2*startVal[row,1]),
                                  startVal[row,2]-abs(2*startVal[row,2]),
                                  startVal[row,3]-abs(1.5*startVal[row,3]),
                                  startVal[row,4]-abs(2*startVal[row,4])),
                        upper = c(startVal[row,1]+abs(2*startVal[row,1]),
                                  startVal[row,2]+abs(2*startVal[row,2]),
                                  startVal[row,3]+abs(1.5*startVal[row,3]),
                                  startVal[row,4]+abs(2*startVal[row,4])),
                        control = nls.lm.control(maxiter = 400)),
                  silent = TRUE)
  
    if (class(gomFit) != "try-error"){
      gomStats[row,] <- c(AIC(gomFit),
                         BIC(gomFit),
                         coef(gomFit)['N0'],
                         coef(gomFit)['Nmax'],
                         coef(gomFit)['rmax'],
                         coef(gomFit)['tlag'])
    } else {
      gomStats[row,] <- c(rep(NA, 6))
    }
    
    # baranyi fit
    barFit <- try(nlsLM(PopBio ~ barModel(N0, Nmax, rmax, t = dfSubset$Time, tlag),
                        dfSubset, list(N0 = startVal[row,1],
                                       Nmax = startVal[row,2],
                                       rmax = startVal[row,3],
                                       tlag = startVal[row,4]),
                        lower = c(startVal[row,1]-abs(2*startVal[row,1]),
                                  startVal[row,2]-abs(2*startVal[row,2]),
                                  startVal[row,3]-abs(1.5*startVal[row,3]),
                                  startVal[row,4]-abs(2*startVal[row,4])),
                        upper = c(startVal[row,1]+abs(2*startVal[row,1]),
                                  startVal[row,2]+abs(2*startVal[row,2]),
                                  startVal[row,3]+abs(1.5*startVal[row,3]),
                                  startVal[row,4]+abs(2*startVal[row,4])),
                        control = nls.lm.control(maxiter = 400)),
                  silent = TRUE)
    
    if (class(barFit) != "try-error"){
      barStats[row,] <- c(AIC(barFit),
                         BIC(barFit),
                         coef(barFit)['N0'],
                         coef(barFit)['Nmax'],
                         coef(barFit)['rmax'],
                         coef(barFit)['tlag'])
    } else {
      barStats[row,] <- c(rep(NA, 6))
    }
  }
  
  # save stats to fitStats
  fitStats[i,] <- c(as.character(dfSubset$Species[1]),
                    as.numeric(dfSubset$numID[1]),
                    as.numeric(dfSubset$Temp[1]),
                    dfSubset$Medium[1],
                    polyStats[i,1], polyStats[i,2],
                    min(logiStats$logiAIC, na.rm = TRUE),
                    logiStats$logiBIC[match(min(logiStats$logiAIC, na.rm = TRUE), logiStats$logiAIC)],
                    min(gomStats$gomAIC, na.rm = TRUE),
                    gomStats$gomBIC[match(min(gomStats$gomAIC, na.rm = TRUE), gomStats$gomAIC)],
                    min(barStats$barAIC, na.rm = TRUE),
                    barStats$barBIC[match(min(barStats$barAIC, na.rm = TRUE), barStats$barAIC)])
  
  fitPara[i,] <- c(as.numeric(dfSubset$numID[1]),
                   polyStats[i,3],
                   polyStats[i,4],
                   polyStats[i,5],
                   polyStats[i,6],
                   logiStats$logiN0[match(min(logiStats$logiAIC, na.rm = TRUE), logiStats$logiAIC)],
                   logiStats$logiNmax[match(min(logiStats$logiAIC, na.rm = TRUE), logiStats$logiAIC)],
                   logiStats$logiRmax[match(min(logiStats$logiAIC, na.rm = TRUE), logiStats$logiAIC)],
                   gomStats$gomN0[match(min(gomStats$gomAIC, na.rm = TRUE), gomStats$gomAIC)],
                   gomStats$gomNmax[match(min(gomStats$gomAIC, na.rm = TRUE), gomStats$gomAIC)],
                   gomStats$gomRmax[match(min(gomStats$gomAIC, na.rm = TRUE), gomStats$gomAIC)],
                   gomStats$gomTlag[match(min(gomStats$gomAIC, na.rm = TRUE), gomStats$gomAIC)],
                   barStats$barN0[match(min(barStats$barAIC, na.rm = TRUE), barStats$barAIC)],
                   barStats$barNmax[match(min(barStats$barAIC, na.rm = TRUE), barStats$barAIC)],
                   barStats$barRmax[match(min(barStats$barAIC, na.rm = TRUE), barStats$barAIC)],
                   barStats$barTlag[match(min(barStats$barAIC, na.rm = TRUE), barStats$barAIC)]
                   )
}

# write to csv for later analysis
write.csv(fitPara, "../Data/fitPara.csv")
write.csv(fitStats, "../Data/fitStats2.csv")
