# MiniProject

*Author: Yewshen Lim*

This directory contains the scripts, data and results for the MiniProject

Languages used in this week:
1. Python
2. R
3. LaTex
4. Bash

Requirements:
1. Python3
    - pandas
2. R v 3.6 and above
    - minpack.lm
    - tidyverse
    - DescTools
    - janitor
    - ggpubr

## Scripts

### 1. `exploration.py`

This script performs exploratory data analysis.

### 2. `models.R`

This script contains the functions for the models to be used in the analysis.

### 3. `modelappy.R`

This script applies the models to the cleaned dataframe to idenfity the best fits and records the parameters.

### 4. `analysis.R`

This script performs analysis on the output of modelapply.R, and also plots the relevant graphs for the report.

### 5. `report.tex & report.bib`

These scripts are to be compiled into the pdf report.

### 6. `run.sh`

This script runs the miniproject from scratch and compiles the report LaTex file, producing a writeup.
