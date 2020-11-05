# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: PP_Regress.R
# Created: Nov 2020
#
# Script draws and saves a pdf of regression analysis using data subsetted by
# the Predator.lifestage field and writes the accompanying regression results to
# a formatted table in csv in the results directory

# clear out workspace
rm(list = ls())

require(ggplot2)
require(dplyr)
require(tidyr)
require(broom)

# load data
df <- read.csv("../Data/EcolArchives-E089-51-D1.csv")
dplyr::glimpse(df)

# convert masses in mg to g
for (i in 1:nrow(df)){
  if (df$Prey.mass.unit[i] == "mg"){
    df$Prey.mass.unit[i] <- "g"
    df$Prey.mass[i] <- df$Prey.mass[i] / 1000
  }
}

# plot the predator against prey mass by feeding type and predator lifestage
# using the linear model method
p <- qplot(Prey.mass, Predator.mass, data = df, log="xy",
           xlab = "Prey mass in grams",
           ylab = "Predator mass in grams",
           colour = Predator.lifestage,
           shape = I(3)) +
       geom_smooth(method = "lm", fullrange = TRUE) + # plot linear regressions
       # facet by feeding interaction
       facet_grid(Type.of.feeding.interaction ~ .) +
       theme_bw() +
       theme(legend.position = "bottom",
             panel.border = element_rect(colour = "grey", fill = NA)) +
       guides(colour = guide_legend(nrow = 1)) + # legend on one line
       theme(legend.title = element_text(size = 8, face="bold"),
             panel.border = element_rect(colour = "black", fill = NA,
                                         size = 0.2))

pdf("../Results/PP_Regress_Results.pdf")
p
dev.off()

# calculate the regression
linreg <- df %>%
          group_by(Type.of.feeding.interaction, Predator.lifestage) %>%
          do(tidy(lm(log(Predator.mass) ~ log(Prey.mass), .)))

# linreg returns:
# piscivorous postlarva/juvenile Prey.mass NA NA NA NA
# planktivorous juvenile Prey.mass 6.557377e+03 NaN NaN NaN

# change Type of feeding interaction and Predator lifestage into factors
df$Type.of.feeding.interaction <- as.factor(df$Type.of.feeding.interaction)
df$Predator.lifestage <- as.factor(df$Predator.lifestage)
# subset the corresponding factors which produced NA and NaN results
ss1 <- df[which(df$Type.of.feeding.interaction == "piscivorous" &
                df$Predator.lifestage == "postlarva/juvenile"), ]
ss2 <- df[which(df$Type.of.feeding.interaction == "planktivorous" &
                df$Predator.lifestage == "juvenile"), ]

linregb <- df %>%
  # filtering entries found in the above subsets
  filter(!Record.number %in% c(30914, 30929, 277, 321)) %>%
  # select columns required and group by feeding type and predator lifestage
  dplyr::select(Predator.mass, Prey.mass, Predator.lifestage,
                Type.of.feeding.interaction) %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage) %>%
  # lm calculation and store calculations to a dataframe
  do(mod = lm(log(Predator.mass) ~ log(Prey.mass), data = .)) %>%
  mutate(Regression.slope = summary(mod)$coeff[2],
         Regression.intercept = summary(mod)$coeff[1],
         R.squared = summary(mod)$adj.r.squared,
         F.statistic = summary(mod)$fstatistic[1],
         p.value = summary(mod)$coeff[8]) %>%
  # remove mod column
  dplyr::select(-mod)

write.csv(linregb, "../Results/PP_Regress_Results.csv")