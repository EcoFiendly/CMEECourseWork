#!/usr/bin/env python3

"""
Script illustrates the use of subprocess to run a Rscript TestR.R
"""

__appname__ = '[TestR.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

import subprocess

subprocess.Popen("Rscript --verbose TestR.R > \
    ../Results/TestR.Rout 2> \
    ../Results/TestR_errFile.Rout", shell = True).wait()