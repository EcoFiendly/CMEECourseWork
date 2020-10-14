#!/bin/bash
# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: tiff2png.sh
# Desc: converts the provided tiff file to png file
# Arguments: 1 tiff file 
# Date: Oct 2020

if [ "$1" == "" ] # check if an argument was provided
then
    echo "Please enter a tiff file and its path as a cli argument"
    exit
elif [[ "$1" != *.tif ]] # check if argument provided was the right file type
then
    echo "Please enter a tiff file"
    exit
else
    # If tiff file was provided
    for f in $1;
        do
            echo "Converting $f";
            out="${f%tif}png" # replace "tif" with "png"
            convert "$f" "$out";
            echo "Moving output to ../Results/"
            mv $out ../Results/ # moves output to Results directory
            echo "Done!"
        done
    exit
fi

#example to consider:
#if [ -f *.tif ]; # looks for tiff files in directory
#then 
#    for f in *.tif # for loop to convert the file
#    do
#        echo "Converting $f"
#        convert "$f"  "$(basename "$f" .tif).jpg"
#    done
#else # if no tiff files
#    echo "There is no .tif file in this directory"
#    exit
#fi
#exit