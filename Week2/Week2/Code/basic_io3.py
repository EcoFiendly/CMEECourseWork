# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: basic_io3.py
# Desc: basic storing objects
# Arguments:
# Date: Oct 2020

#################################
# STORING OBJECTS 
#################################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle
f = open('../Sandbox/testp.p', 'wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
f = open('../Sandbox/testp.p', 'rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)