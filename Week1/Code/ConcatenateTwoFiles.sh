#!/bin/bash
# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: ConcatenateTwoFiles.sh
# Description: concatenate two separate files into one
# Arguments: first file, second file, resulting file
# Date: Oct 2020

# Check if arguments are provided
if [ "$1" == "" ] || [ "$2" == "" ] || [ "$3" == "" ]
then
    echo "Please provide files and name the output file"
else
    cat $1 > $3 # concatenate and print $1, then redirected into $3
    cat $2 >> $3 # concatenate and print $2, then redirected into $3
    echo "Merged file is $3"
    cat $3 # concatenate and print $3
    echo
    echo "Moving $3 to ../Data/"
    mv $3 ../Data/ # move $3 to Results directory
fi
exit