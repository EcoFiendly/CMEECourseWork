#!/bin/bash
# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: CountLines.sh
# Description: Count the number of lines present in the file provided 
# Arguments: 1 file
# Date: Oct 2020

# Check if a file is provided
if [ "$1" == ""]
then
    echo "Please provide a file and its path as a cli argument"
else
    # if a file is provided
    NumLines=`wc -l < $1` 
    # wc -l counts the number of lines
    # < redirects the contents of the file to the stdin of command wc -l
    echo "The file $1 has $NumLines lines"
    echo # returns an empty line for readability
fi
exit