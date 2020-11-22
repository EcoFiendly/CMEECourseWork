# Week 3

*Author: Yewshen Lim*

*Created: Week 3*

This directory contains the scripts, data and results from week 7

Languages used in this week:
1. R
2. Python
3. LaTeX
4. Bash

Requirements:
1. R v 3.6 and above
    - tidyverse (which includes ggplot2, reshape2, dplyr, tidyr)
    - maps
2. Python3
    - numpy
    - time
3. LaTeX
4. A terminal running bash

## Scripts

### 1. `basic_io.R`

A simple script to illustrate R input-output

### 2. `control_flow.R`

Script illustrates the use of control flow in R

### 3. `break.R`

Script illustrates how to break out of a loop

### 4. `next.R`

Script illustrates the use of next

### 5. `boilerplate.R`

A boilerplate R script

### 6. `R_conditionals.R`

Script illustrates the use of conditionals

### 7. `TreeHeight.R`

Script contains a function that calculates heights of trees given distance of 
each tree from its base and angle to its top, using the trigonometric formula. 
Script takes input, applies TreeHeight function and writes output to a csv 
file in results

### 8. `Vectorize1.R`

Script illustrates vectorization, where it is an approach which directly 
applies compiled, optimized code to run an operation on a vector, matrix or a 
higher-dimensional data structure (like an R array), instead of performing the 
operation element-wise on the data structure. Script compares the speed between 
the vectorized and non-vectorized functions.

### 9. `preallocate.R`

Script illustrates how preallocation speeds up a loop that resizes a vector 
repeatedly

### 10. `apply1.R`

Script illustrates the use of apply to apply a function to rows/columns of a 
matrix

### 11. `apply2.R`

Script contains a function SomeOperation, which takes an input v, if sum of v 
is greater than zero, the function multiplies that value by 100. So if v has 
positive and negative numbers, and the sum comes out to be positive, only then 
does it multiply all the valus in v by 100 and return them

### 12. `sample.R`

This script illustrates how lapply and sapply work and also how to sample 
random numbers

### 13. `Ricker.R`

This script runs a simulation of the Ricker model and returns a vector of 
length generations

### 14. `Vectorize2.R`

This script runs the stochastic Ricker equation with gaussian fluctuations, 
and the attempt to vectorize the function

### 15. `browse.R`

Script illustrates the use of browser function to debug

### 16. `try.R`

Script illustrates the use of try function to "catch" errors

### 17. `TAutoCorr.R`

Script calculates the correlation between n - 1 pairs of years, where n is the 
total number of years. Generates a plot of the data which is saved as a pdf

### 18. `TAutoCorr.tex`

Script compiles the report which presents the results and interpretation of TAutoCorr.R into a pdf

### 19. `DataWrang.R`

Script uses base R packages to wrangle the Pound Hill Dataset

### 20. `DataWrangTidy.R`

Script uses tidyverse (specifically dplyr and tidyr) for the same data wrangling steps in DataWrang.R

### 21. `PP_Dists.R`

Script draws and saves three figures, each containing subplots of distributions of predator mass, prey mass, and the size ration of prey mass over predator mass by feeding interaction type. Use logarithms of masses (or size ratios) for all three plots. In addition, the script should calculate the (log) mean and median predator mass, prey mass and predator-prey size-ratios to a csv file

### 22. `Girko.R`

Script plots the Girko's law simulation, and saves the resulting figure to the results directory

### 23. `MyBars.R`

Script demonstrates how to annotate a plot and saves the resulting figure to the results directory

### 24. `plotLin.R`

Script demonstrates mathematical annotation on an axis and in the plot area, and saves the resulting figure to the results directory

### 25. `PP_Regress.R`

Script draws and saves a pdf of regression analysis and writes the accompanying regression results to a formatted table in csv in the results directory

### 26. `GPDD_Data.R`

Script creates a world map and superimposes it on all the locations from which data were provided in the GPDD dataframe

## Groupwork

### 1. `Vectorize1.py`

Python version of Vectorize1.R

### 2. `Vectorize2.py`

Python version of Vectorize2.R

### 3. `bashscript to compare speeds`

Script runs Vectorize 1 and 2 in both R and python for speed comparison

### 4. `get_TreeHeight.R`

Script takes an input file, applies the function TreeHeight.R, and outputs the result to a file which includes the input file name, e.g. InputFileName_treeheights.csv

### 5. `run_get_TreeHeight.sh`

Script runs get_TreeHeight.R and get_TreeHeight.py (script below) with the argument trees.csv

### 6. `get_TreeHeight.py`

Python version of get_TreeHeight.R

### 7. `PP_Regress_loc.R`

Script does the same as PP_Regress.R but data is additionally subset by the Location field and only outputs the analysis results to a csv in the results directory