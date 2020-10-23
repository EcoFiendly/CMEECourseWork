# This function calculates heights of trees given distance of each tree from its
# base and angle to its top, using the trigonometric formula
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees: The angle of elevation of tree
# distance: The distance from base of tree (e.ge, meters)
#
# OUTPUT
# othe heights of the tree, same units as "distance"

TreeData <- read.csv("../Data/trees.csv", header = TRUE)

TreeHeight <- function(degrees, distance) {
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    print(paste("Tree height is:", height))

    return(height)
}

TreeData$Tree.Height.m <- TreeHeight(TreeData$Distance.m,
 TreeData$Angle.degrees)

write.csv(TreeData, "../Results/TreeHts.csv")