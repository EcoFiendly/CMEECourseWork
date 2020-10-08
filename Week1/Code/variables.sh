#!/bin/bash
# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: variables.sh
# Desc: examples of assignments
# Arguments: MyVar
# Date: Oct 2020

# Shows the use of variables
# assign value to MyVar
MyVar='some string' 
echo 'the current value of the variable is' $MyVar
echo 'Please enter a new string'
read MyVar
echo 'the current value of the variable is' $MyVar


## Reading multiple values
echo 'Enter two numbers sepaarated by spaces(s)'
read a b
echo 'you entered' $a 'and' $b '. Their sum is:'
mysum=`expr $a + $b`
echo $mysum
