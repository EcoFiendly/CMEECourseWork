#!/usr/bin/env python3

"""
Script illustrates the use of subprocess module to run a Rscript fmr.R

Prints output showing if the run was successful, and the contents of the R 
console output
"""

__appname__ = '[run_fmr_R.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

import subprocess

subprocess.Popen("Rscript fmr.R > \
    ../Results/fmrR.Rout 2> \
    ../Results/fmrR_errFile.Rout", shell = True).wait()

# subprocess.Popen("Rscript --verbose fmr.R", shell = True).wait()

# open error file
with open("../Results/fmrR_errFile.Rout", "r") as f:
    # read error file
    out = f.read()
    # check if run was successful based on contents of error file
    if len(out) > 0:
        print("Run was unsuccessful")
    else:
        print("Run was successful")
        # open and prints content of R console
        with open("../Results/fmrR.Rout", "r") as f2:
            print("\nR console output:\n" + f2.read())