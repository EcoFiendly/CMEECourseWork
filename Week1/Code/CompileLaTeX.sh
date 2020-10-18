#!/bin/bash
# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: CompileLaTeX.sh
# Description: Compiles the given LaTeX file and generates a pdf output
# Arguments: 1 LaTeX file
# Date: Oct 2020

if [ "$1" == "" ] # Check if an argument is provided
then
    echo "Please provide a LaTeX file (without the extension) and its relative path" 
else
    echo "Compiling ..."
    pdflatex $1.tex
    pdflatex $1.tex
    bibtex $1
    pdflatex $1.tex
    pdflatex $1.tex
    #evince $1.pdf & # Samraat uses evince, line can be suppressed

    ## Cleanup
    rm *~
    rm *.aux
    rm *.dvi
    rm *.log
    rm *.nav
    rm *.out
    rm *.snm
    rm *.toc
    rm *.bbl
    rm *.blg
    rm *.fls

    echo "Done!"
fi
exit