# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: basic_io2.py
# Desc: basic output
# Arguments:
# Date: Oct 2020

#################################
# FILE OUPUT
#################################
# Save the elements of a list to a file
list_to_save = range(100)

f = open('../Sandbox/testout.txt', 'w')
for i in list_to_save:
    f.write(str(i) + '\n')  ## oadd a new line at the end

f.close()