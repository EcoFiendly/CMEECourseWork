#!/bin/bash

# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: run.sh
# Created: Jan 2021

# This script runs the miniproject from scratch and compiles the report LaTeX 
# file, producing a writeup in pdf

echo "Starting miniproject workflow"

# run exploration.py
echo "Running exploratory analysis on data"
python3 -W ignore exploration.py
echo "Exploratory analysis complete"

# run model fitting script
echo "Applying models to data"
Rscript --no-echo modelapply.R > silent.out 2> silent.out
echo "Application complete"

# run analysis script
echo "Performing analysis on outputs of model application"
Rscript --no-echo analysis.R > silent.out 2> silent.out
echo "Completed analysis"

# compile LaTeX file
echo "Compiling report.tex"
pdflatex -quiet=true --interaction=batchmode report.tex > silent.out 2> silent.out
bibtex report > silent.out 2> silent.out
pdflatex -quiet=true --interaction=batchmode report.tex > silent.out 2> silent.out
bibtex report > silent.out 2> silent.out
pdflatex -quiet=true --interaction=batchmode report.tex > silent.out 2> silent.out
pdflatex -quiet=true --interaction=batchmode report.tex > silent.out 2> silent.out
# move report into ../Results/
mv report.pdf ../Results/report.pdf
echo "Compilation complete, report available in ../Results/"

# cleanup
rm *.log
rm *.bbl
rm *.xml
rm *-blx.bib
rm *.aux
rm *.blg
rm Rplots.pdf
rm *.out

# announce completion of script
echo "Workflow complete!"
