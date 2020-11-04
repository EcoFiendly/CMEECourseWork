# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: DataWrangTidy.R
# Created: Oct 2020
#
# Script uses dplyr and tidyr to wrangle the Pound Hill Dataset

################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################

require(dplyr)
require(tidyr)

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../data/PoundHillData.csv", header = FALSE))

# header = true because we do have metadata headers
MyMetaData <- read.csv("../data/PoundHillMetaData.csv", header = TRUE, sep = ";")

############# Inspect the dataset ###############
head(MyData)
dim(MyData)
dplyr::glimpse(MyData) # tidier str()

############# Transpose ###############
# To get those species into columns and treatments into rows 
MyData <- t(MyData)
head(MyData)
dim(MyData)

############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1, ], stringsAsFactors = F) 
#stringsAsFactors = F is important!
colnames(TempData) <- MyData[1, ] # assign column names from original data

############# Convert from wide to long format  ###############

# using dplyr
MyWrangledData <- TempData %>% 
    gather(Species, Count, -Cultivation, -Block, -Plot, -Quadrat)

# set Cultivation, Block, Plot, Quadrat columns as factors and count as numeric
MyWrangledData <- MyWrangledData %>%
    mutate(Cultivation = factor(Cultivation),
           Block = factor(Block),
           Plot = factor(Plot),
           Quadrat = factor(Quadrat),
           Count = as.integer(Count))

dplyr::glimpse(MyWrangledData)
head(MyWrangledData)
dim(MyWrangledData)

############# Exploring the data (extend the script below)  ###############
