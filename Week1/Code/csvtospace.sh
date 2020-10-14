#!/bin/bash
# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: csvtospace.sh
# Description: takes csv files and converts it to space separated values file 
#
# Saves the output into a .txt file
# Arguments: 1 csv file
# Date: Oct 2020

# Check if a csv file is provided
#if [ "$1" == ""]
#then
#    echo "Please enter a csv file and its path as a cli argument"
#    exit
#else
#    # If a csv file is provided
#    echo "Creating a space separated version of $1"
#    out="${1%csv}txt" # replace "csv" with "txt"
#    cat $1 | tr -s "," " " >> $out # substitutes commas with spaces
#    echo "Moving output to ../Results"
#    mv $out ../Results # moves output to Results directory
#    echo "Done!"
#    exit
#fi
if [ "$1" == "" ] # check if argument was provided
then
    echo "Enter relative path where csv files are located:"
    read PathVar # assigns argument as variable
    for f in $PathVar/*.csv; # for loop looks for .csv files in directory
        do
            echo "Creating space separated versions of $f";
            out="${f%csv}txt" # replace "csv" with "txt"
            cat $f | tr -s "," " " >> $out # substitute commas with space and saves to output file
            echo "Moving outputs to ../Results"
            mv $out ../Results # moves output to Results directory
            echo "Done!"
        done
    exit
fi