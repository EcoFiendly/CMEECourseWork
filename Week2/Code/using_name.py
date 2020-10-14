#!/usr/bin/env python3
# Filename: using_name.py

"""
Script is used to illustrate '__name__ == "__main__"'
This line directs the python interpreter to set the special __name_ variable to
have a value "__main__", so that the file is usable as a script as well as an 
importable module.
On the other hand, if some other module is the main program and your module is 
being imported, the interpreter looks at the filename of your module, strips off
the .py and assigns that string to the module's __name__ variable instead, 
skipping the command(s) under the if statement.
"""

__appname__ = '[using_name.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## Functions ##
if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")

print("This module's name is: " + __name__)