# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: analysis.R
# Created: Dec 2020
#
# This script performs analysis on the output of modelapply.R, and also plots
# the relevant graphs for the report.

# temporarily setwd for ease of use
setwd("~/CMEECourseWork/MiniProject/Code")

rm(list=ls())

# packages
library("tidyverse")
library("DescTools")
library("janitor")
library("ggpubr")
source("models.R")

# load files
fitStats <- read.csv("../Data/fitStats2.csv", stringsAsFactors = FALSE)
fitPara <- read.csv("../Data/fitPara.csv", stringsAsFactors = FALSE)

# load prepped data
df <- read.csv("../Data/PreppedLGD.csv")
subsetID <- unique(df$numID)

# keep AIC for comparison
fitStats <- subset(fitStats, select = -c(X, polyBIC, logiBIC, gomBIC, barBIC))

# record the best model
fitStats$model <- colnames(fitStats[,5:8])[apply(fitStats[,5:8], 1, which.min)]

# replace model names
fitStats$model[fitStats$model == "polyAIC"] <- "Cubic"
fitStats$model[fitStats$model == "logiAIC"] <- "Logistic"
fitStats$model[fitStats$model == "gomAIC"] <- "Modified Gompertz"
fitStats$model[fitStats$model == "barAIC"] <- "Baranyi"

# replace Inf with NA
fitStats$logiAIC[fitStats$logiAIC == Inf] <- NA
fitStats$gomAIC[fitStats$gomAIC == Inf] <- NA
fitStats$barAIC[fitStats$barAIC == Inf] <- NA

################################################################
# Plot percentage of fit on all datasets
################################################################
# open device
png("../Results/totFit.png")
# plot
barplot(c("Cubic" = length(na.omit(fitStats$polyAIC)),
  "Logistic" = length(na.omit(fitStats$logiAIC)),
  "Modified Gompertz" = length(na.omit(fitStats$gomAIC)),
  "Baranyi" = length(na.omit(fitStats$barAIC)))/299*100,
  ylim = c(0,100),
  cex.names = 0.8,
  xlab = "Model",
  ylab = "Total percentage of fit (%)"
)
dev.off()

######################################################################
# plot percentage of best fits per model
######################################################################
png("../Results/bestFit.png")
 
barplot(sort(table(fitStats$model)/sum(table(fitStats$model)) * 100, decreasing = T),
        ylim = c(0,50), cex.names = 0.8,
        xlab = "Model", ylab = "Percentage of best fit (%)")
dev.off()

#####################################################################
# plot ID 250 as general figure
#####################################################################
png("../Results/genShape.png")

dfSubset <- df[which(df$numID == subsetID[251]),]
dfSubset$PopBio <- log10(dfSubset$PopBio)
t <- seq(min(dfSubset$Time), max(dfSubset$Time),
        (max(dfSubset$Time) - min(dfSubset$Time))/1000)
gomF <- gomModel(fitPara[251,]$gomN0, fitPara[251,]$gomNmax, fitPara[251,]$gomRmax, t, fitPara[251,]$gomTlag)
g <- ggplot(dfSubset, aes(Time, PopBio)) +
     xlab("Time (Hours)") +
     ylab("Population Bio (log)") +
     geom_line(data.frame(t, gomF), mapping = aes(t, gomF)) +
     annotate("segment",
              color = "red",
              x = 100, xend = 350,
              y = 2.26 , yend = 2.26,
              linetype = "dashed") +
     annotate("text",
              label = "Stationary phase at carrying capacity",
              y = 2.3, x = 0,
              hjust = 0,
              color = "red") +
     annotate("segment",
              color = "green",
              x = 0, xend = 200,
              y = 0.41, yend = 0.41,
              linetype = "dashed") +
     annotate("text",
              label = "Lag phase at minimum population",
              y = 0.46, x = 200,
              color = "green") +
     annotate("segment",
              color = "blue",
              x = 86, xend = 169,
              y = 0.30, yend = 2.4,
              linetype = "dashed") +
     annotate("text",
              label = "Maximum growth rate",
              y = 1.25, x = 190,
              colour = "blue") +
     theme(axis.text.x = element_blank(),
           axis.text.y = element_blank(),
           axis.ticks.x = element_blank(),
           axis.ticks.y = element_blank(),
           panel.grid = element_blank(),
           panel.background = element_blank(),
           axis.line = element_line(color = "black"))
print(g)
dev.off()

########################################################################
# Goodness of fits tests
########################################################################
# create new column for type of model
fitStats$modelType <- ifelse((fitStats$model == "Baranyi"), "Mechanistic", "Phenomenological")

# G-test
observed <- as.vector(table(fitStats$modelType))
expected <- c(0.5,0.5)
GTest(x = observed,
      p = expected,
      correct = "none")

# chisqr test
chisq.test(x = observed,
           p = expected)

# bin temps into <10, 10<20, and >20
fitStats$Temp2 <- as.factor(ifelse((fitStats$Temp < 11), "1-10", ifelse(fitStats$Temp < 21, "11-20", "21-30")))
# tally for bins
tempStats <- fitStats %>%
  tabyl(Temp2, model) %>%
  adorn_totals("row") %>%
  adorn_percentages("row") %>%
  adorn_pct_formatting(rounding = "half up", digits = 1) %>%
  adorn_ns() %>%
  rename("Temperature Bins (degress celcius)" = "Temp2")

write.csv(tempStats, "../Results/tempStats.csv", quote = F)

# G-test
observed <- as.vector(table(fitStats$Temp2, fitStats$model)[,1])
expected <- c(0.333,0.333,0.333)
GTest(x = observed,
      p = expected,
      correct = "none")
observed <- as.vector(table(fitStats$Temp2, fitStats$model)[,2])
expected <- c(0.333,0.333,0.333)
GTest(x = observed,
      p = expected,
      correct = "none")
observed <- as.vector(table(fitStats$Temp2, fitStats$model)[,3])
expected <- c(0.333,0.333,0.333)
GTest(x = observed,
      p = expected,
      correct = "none")
observed <- as.vector(table(fitStats$Temp2, fitStats$model)[,4])
expected <- c(0.333,0.333,0.333)
GTest(x = observed,
      p = expected,
      correct = "none")

# model tally for different mediums
liquids <- c("APT Broth", 
               "ESAW",
               "MRS broth",
               "Pasteurised Double Cream",
               "Pasteurised Full-fat Milk",
               "Pasteurised Skim Milk",
               "TSB",
               "UHT Double Cream",
               "UHT Full-fat Milk",
               "UHT Skim Milk",
               "Z8")
fitStats$Medium2 <- as.factor(ifelse(fitStats$Medium %in% liquids, "Liquid", "Solid"))

# tally for bins
mediumStats <- fitStats %>%
  tabyl(Medium2, model) %>%
  adorn_totals("row") %>%
  adorn_percentages("row") %>%
  adorn_pct_formatting(rounding = "half up", digits = 1) %>%
  adorn_ns() %>%
  rename("Medium State" = "Medium2")

write.csv(mediumStats, "../Results/mediumStats.csv", quote = F)

# exact test of goodness of fit on model performance
binom.test(table(fitStats$Medium2, fitStats$model)[1,1], sum(table(fitStats$Medium2, fitStats$model)[,1]), 0.5,
           alternative = "less",
           conf.level = 0.95)
binom.test(table(fitStats$Medium2, fitStats$model)[1,2], sum(table(fitStats$Medium2, fitStats$model)[,2]), 0.5,
           alternative = "less",
           conf.level = 0.95)
binom.test(table(fitStats$Medium2, fitStats$model)[1,3], sum(table(fitStats$Medium2, fitStats$model)[,3]), 0.5,
           alternative = "less",
           conf.level = 0.95)
binom.test(table(fitStats$Medium2, fitStats$model)[1,4], sum(table(fitStats$Medium2, fitStats$model)[,4]), 0.5,
           alternative = "less",
           conf.level = 0.95)

# plot Staphylococcus spp at 6 different temperatures
dfTemps <- df[which(df$Species == "Staphylococcus spp."),]
dfTemps <- dfTemps[which(dfTemps$Medium == "Raw Chicken Breast"),]
plotList <- list()
j <- 1
for (i in unique(dfTemps$numID)){
  dfSubset <- dfTemps[which(dfTemps$numID == i),]
  dfSubset$PopBio <- log10(dfSubset$PopBio)
  # define sequence of Time
  t <- seq(min(dfSubset$Time), max(dfSubset$Time),
           (max(dfSubset$Time) - min(dfSubset$Time))/1000)
  # plot each curve on subset
  p <- ggplot(dfSubset, aes(Time, PopBio)) +
    # ggtitle(paste0("ID ", i, ", ", "Temperature = ", dfSubset$Temp[1], "\u00B0C")) +
    xlab(NULL) +
    ylab(NULL) +
    geom_point() 
  
  i = i+1
  if (is.na(fitPara[i,]$a) == FALSE){
    polyF <- fitPara[i,]$a*t^3 + fitPara[i,]$b*t^2 + fitPara[i,]$c*t + fitPara[i,]$d
    p = p + geom_line(data.frame(t, polyF), mapping = aes(t, polyF, colour = "Cubic"))
  }
  if (is.na(fitPara[i,]$logiN0) == FALSE){
    # logi fit
    logiF <- logModel(fitPara[i,]$logiN0, fitPara[i,]$logiNmax, fitPara[i,]$logiRmax, t)
    p = p + geom_line(data.frame(t, logiF), mapping = aes(t, logiF, colour = "Logistic"))
  }
  if (is.na(fitPara[i,]$gomN0) == FALSE){
    # gom fit
    gomF <- gomModel(fitPara[i,]$gomN0, fitPara[i,]$gomNmax, fitPara[i,]$gomRmax, t, fitPara[i,]$gomTlag)
    p = p + geom_line(data.frame(t, gomF), mapping = aes(t, gomF, colour = "Gompertz"))
  }
  if (is.na(fitPara[i,]$barN0) == FALSE){
    # bar fit
    barF <- barModel(fitPara[i,]$barN0, fitPara[i,]$barNmax, fitPara[i,]$barRmax, t, fitPara[i,]$barTlag)
    p = p + geom_line(data.frame(t, barF), mapping = aes(t, barF, colour = "Baranyi"))
  }

  p <- p + theme(legend.position = "bottom")

  p <- p + scale_color_manual("",
                       breaks = c("Cubic", "Logistic", "Gompertz", "Baranyi"),
                       values = c("Cyan", "Magenta", "Yellow", "Black"))
  
  plotList[[j]] <- p
  j <- j + 1
}

p1 <- ggarrange(plotList[[1]], plotList[[2]], plotList[[3]],
          plotList[[4]], plotList[[5]], plotList[[6]],
          labels = c("2 \u00B0C", "4 \u00B0C", "7 \u00B0C",
                     "10 \u00B0C", "15 \u00B0C", "20 \u00B0C"),
          common.legend = TRUE, legend = "top")

p1 <- annotate_figure(p1,
                left = text_grob(expression("Population Bio (log"[10]*")"), rot = 90),
                bottom = text_grob("Time (Hours)"))

ggsave(paste("../Results/diffTemps.png"), plot = p1, device = png())

# # plot individual IDs and fits
# for (i in 1:length(subsetID)){
#   dfSubset <- df[which(df$numID == subsetID[i]),]
#   dfSubset$PopBio <- log10(dfSubset$PopBio)
# 
#   # define sequence of Time
#   t <- seq(min(dfSubset$Time), max(dfSubset$Time),
#            (max(dfSubset$Time) - min(dfSubset$Time))/1000)
# 
#   # plot each curve on subset
#   p <- ggplot(dfSubset, aes(Time, PopBio)) +
#     ggtitle(paste("ID", i-1)) +
#     xlab("Time (Hours)") +
#     ylab(expression("Population Bio (log"[10]*")")) +
#     geom_point()
# 
#   if (is.na(fitPara[i,]$a) == FALSE){
#     polyF <- fitPara[i,]$a*t^3 + fitPara[i,]$b*t^2 + fitPara[i,]$c*t + fitPara[i,]$d
#     p = p + geom_line(data.frame(t, polyF), mapping = aes(t, polyF, colour = "Cubic"))
#   }
#   if (is.na(fitPara[i,]$logiN0) == FALSE){
#     # logi fit
#     logiF <- logModel(fitPara[i,]$logiN0, fitPara[i,]$logiNmax, fitPara[i,]$logiRmax, t)
#     p = p + geom_line(data.frame(t, logiF), mapping = aes(t, logiF, colour = "Logistic"))
#   }
#   if (is.na(fitPara[i,]$gomN0) == FALSE){
#     # gom fit
#     gomF <- gomModel(fitPara[i,]$gomN0, fitPara[i,]$gomNmax, fitPara[i,]$gomRmax, t, fitPara[i,]$gomTlag)
#     p = p + geom_line(data.frame(t, gomF), mapping = aes(t, gomF, colour = "Gompertz"))
#   }
#   if (is.na(fitPara[i,]$barN0) == FALSE){
#     # bar fit
#     barF <- barModel(fitPara[i,]$barN0, fitPara[i,]$barNmax, fitPara[i,]$barRmax, t, fitPara[i,]$barTlag)
#     p = p + geom_line(data.frame(t, barF), mapping = aes(t, barF, colour = "Baranyi"))
#   }
# 
#   p <- p + theme(legend.position = "bottom")
# 
#   p <- p + scale_color_manual("",
#                        breaks = c("Cubic", "Logistic", "Gompertz", "Baranyi"),
#                        values = c("Cyan", "Magenta", "Yellow", "Black"))
# 
#   ggsave(paste("../Results/Plots/ID_", i-1, ".png", sep = "", device = png()))
# 
#   dev.off()
# }
