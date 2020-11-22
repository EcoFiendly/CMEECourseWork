# Week 7

*Author: Yewshen Lim*

*Created: Week 7*

This directory contains the scripts, data and results from week 7

Languages used in this week:
1. Python
2. R

Requirements:
1. Python3
    - numpy
    - scipy
    - pandas
    - re
2. IPython 7
    -timeit
3. R v 3.6 and above
4. A terminal running bash

## Scripts

### 1. `LV1.py`

Script illustrates the use of numerical integration to solve the Lotka-Volterra 
model

### 2. `LV2.py`

Script illustrates the use of numerical integration to solve the Lotka-Volterra 
model with the addition of K, the carrying capacity, along with taking user 
inputs for r, a, z, e

### 3. `profileme.py`

Script illustrates the use of profiling on three functions
my_squares(iters) squares the input by the number of iters (iterations)
my_join(iters, string) joins the strings together by number of iters
run_my_funcs(x, y) runs the other two functions

### 4. `profileme2.py`

Script profiles the vectorized versions of my_squares and my_join from 
profileme.py

### 5. `timeitme.ipy`

Script illustrates the use if timeit, an ipython magic command, to compare the 
speed of loops and list comprehensions
Run with ipython from cli
Functions for comparison are imported from profileme.py and profileme2.py

### 6. `run_LV.py`

Script illustrates the use of cProfile to profile LV1.py, LV2.py and LV3.py
Prints first 50 rows sorted by total time for each profile

### 7. `regexs.py`

Script illustrates the use of regex

### 8. `blackbirds.py`

Script illustrates the use of regex to capture Kingdom, Phylum and Species names
from an input file containing taxonimic information of blackbirds

### 9. `TestR.R`

Script prints one string

### 10. `TestR.py`

Script illustrates the use of subprocess to run a Rscript TestR.R

### 11. `using_os.py`

Script illustrates the use of subprocess.os module to get a list of files and
directories in the CMEECourseWork directory

### 12. `fmr.R`

Script plots log(field metabolic rate) against log(body mass) for the Nagy et 
al 1999 dataset to a file fmr.pdf

### 13. `run_fmr_R.py`

Script illustrates the use of subprocess module to run a Rscript fmr.R

Prints output showing if the run was successful, and the contents of the R 
console output

## Groupwork

### 1. `LV3.py`

Script runs the discrete-time version of the Lotka-Volterra model and plots the 
results in two graphs saved to ../Results.