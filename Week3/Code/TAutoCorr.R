# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: TAutoCorr.R
# Created: Oct 2020
#
# This script calculates the correlation between n - 1 pairs of years, where n
# is the total number of years. Generates a plot of the data which is saved as a
# pdf

# clear out workspace
rm(list = ls())

# set seed so results are reproducible
set.seed(1)

# load data
load("../Data/KeyWestAnnualMeanTemperature.RData")

# list the structure
ls.str(ats)

# plot
pdf("../Results/TACplot1.pdf")
plot(ats$Year, ats$Temp,
    xlab = "Year",
    ylab = "Temp (Degrees celcius)",
    type = "p")
dev.off()

# overall correlation
# compute the correlation between successive years T[y] against T[y+1]
# temp in y+1 is dependent on temp in y
T_y0 <- c(ats[1:99, 2])
T_y1 <- c(ats[2:100, 2])
cc0 <- cor(T_y0, T_y1)
cat("The correlation between successive years is", cc0)

# generating 10000 samples of random ordered temperatures
samples <- replicate(10000, sample(ats$Temp, replace = F))

# generate a vector of corr coeffs from the 10000 random samples
ccS <- vector("numeric", 10000)
for (i in 1:10000) {
    T_s <- cor(samples[1:99, i], samples[2:100, i])
    ccS[i] <- T_s
}

# histogram to compare coefficient correlations
pdf("../Results/TACplot2.pdf")
hist(ccS, xlim = c(-0.4, 0.4),
    xlab = "Correlation coefficients of random sample",
    main = NULL)
abline(v = cc0, col = "red", lwd = 1, lty = 2)
text(cc0 - 0.1, 1875, "original correlation coefficient \nfor successive years")
dev.off()

# calculating the estimated p-value
p_estimate <- sum(ccS > cc0) / 10000
cat("The estimated p-value is", p_estimate)