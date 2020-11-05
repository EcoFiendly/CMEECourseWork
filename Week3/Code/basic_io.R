# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: basic_io.R
# Created: Oct 2020
#
# A simple script to illustrate R input-output
# Run line by line and check inputs outputs to understand what is happening

rm(list = ls())

MyData <- read.csv("../Data/trees.csv", header = TRUE) # import with headers

write.csv(MyData, "../Results/MyData.csv") # write it out as a new file

# append to it
write.table(MyData[1, ], file = "../Results/MyData.csv", append = TRUE)

write.csv(MyData, "../Results/MyData.csv", row.names = TRUE) # write row names

# ignore column names
write.table(MyData, "../Results/MyData.csv", col.names = FALSE)

print("Script complete!")