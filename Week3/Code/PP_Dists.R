# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: PP_Dists.R
# Created: Oct 2020
#
# This script draws and saves three figures, each containing subplots of
# distributions of predator mass, prey mass, and the size ratio of prey mass
# over predator mass by feeding interaction type. Use logarithms of masses
# (or size ratios) for all three plots. In addition, the script should calculate
# the (log) mean and median predator mass, prey mass and predator-prey
# size-ratios to a csv file

# clear out workspace
rm(list = ls())

# packages
require(dplyr)

# load data
df <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

# explore data
dim(df)
dplyr::glimpse(df)

# convert masses from mg to g
for (i in 1:nrow(df)){
  if (df$Prey.mass.unit[i] == "mg"){
    df$Prey.mass.unit[i] = "g"
    df$Prey.mass[i] = df$Prey.mass[i] / 1000
  }
}

# pred subplots.pdf
pdf("../Results/Pred_Subplots.pdf")
par(mfrow = c(2, 3))
for (i in unique(df$Type.of.feeding.interaction)) {
  j <- subset(df, Type.of.feeding.interaction == i)
  plot(density(log(j$Predator.mass)), main = i, col = "steelblue", frame = F,
       xlab = "log of Predator mass",
       xlim = c(-10, 10),
       ylim = c(0.0, 0.4))
}
dev.off()

# prey subplots.pdf
pdf("../Results/Prey_Subplots.pdf")
par(mfrow = c(2, 3))
for (i in unique(df$Type.of.feeding.interaction)) {
  j <- subset(df, Type.of.feeding.interaction == i)
  plot(density(log(j$Prey.mass)), main = i, col = "steelblue", frame = F,
       xlab = "log of Prey mass",
       xlim = c(-20, 10),
       ylim = c(0.0, 0.4))
}
dev.off()

# size ratio_subplots.pdf
pdf("../Results/SizeRatio_Subplots.pdf")
par(mfrow = c(2, 3))
for (i in unique(df$Type.of.feeding.interaction)) {
  j <- subset(df, Type.of.feeding.interaction == i)
  plot(density(log(j$Prey.mass/j$Predator.mass)), main = i, col = "steelblue",
       frame = F,
       xlab = "log of Prey mass / Predator mass",
       xlim = c(-20, 5),
       ylim = c(0.0, 0.35))
}
dev.off()

# pp_results.csv
stats <- df %>%
  group_by(Type.of.feeding.interaction) %>%
  summarise(mean(log(Predator.mass)),
            median(log(Predator.mass)),
            mean(log(Prey.mass)),
            median(log(Prey.mass)),
            mean(log(Prey.mass / Predator.mass)),
            median(log(Prey.mass / Predator.mass)))
# name the columns
names(stats) <- c("Type.of.feeding.interaction",
                  "Mean.log.predator.mass",
                  "Median.log.predator.mass",
                  "Mean.log.prey.mass",
                  "Median.log.prey.mass",
                  "Mean.log.ratio.prey.predator.mass",
                  "Median.log.ratio.prey.predator.mass")
# write to csv
write.csv(stats, "../Results/PP_Results.csv")