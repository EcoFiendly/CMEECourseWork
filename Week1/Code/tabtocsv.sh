#!/bin/bash
# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: tabtocsv.sh
# Description: substitute the tabs with commas in the file provided 
#
# Saves the output into a .csv file
# Arguments: 1 tab delimited file
# Date: Oct 2020

if [ "$1" == "" ] # check if an argument is provided
then
    echo "Please enter a tab separated file and its path as a cli argument"
    exit
elif [[ "$1" != *.txt ]]
then
    echo "Please enter a txt file" # check if argument was provided and if it was the right file type
    exit
else
    # If a txt file is provided
    echo "Creating a comma delimited version of $1 ..."
    out="${1%txt}csv" # replace "txt" with "csv"
    cat $1 | tr -s "\t" "," >> $out # substitute tabs with commas, and saves to output file
    echo "Moving output to ../Results/"
    mv $out ../Results/ # moves output to Results directory
    echo "Done!"
    exit
fi