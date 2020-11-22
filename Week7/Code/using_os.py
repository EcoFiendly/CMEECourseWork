#!/usr/bin/env python3

"""
Script illustrates the use of subprocess.os module to get a list of files and
directories in the CMEECourseWork directory
"""

__appname__ = '[using_os.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

import subprocess

# Get list of all files and directories in home
CMEEwd = subprocess.os.path.expanduser("../../")
listOfFiles = list()
for (dirpath, dirnames, filenames) in subprocess.os.walk(CMEEwd):
    listOfFiles += [subprocess.os.path.join(dirpath, file) \
        for file in filenames]

print(listOfFiles)

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:

# Get the user's home directory.
CMEEwd = subprocess.os.path.expanduser("../../")

# Create a list to store the results.
FilesDirsStartingWithC = []

# for loop to append files starting with C to list
for (dirpath, dirnames, filenames) in subprocess.os.walk(CMEEwd):
    FilesDirsStartingWithC += [subprocess.os.path.join(dirpath, file) \
        for file in filenames if file.startswith("C") == True]

print(FilesDirsStartingWithC)

#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

# Type your code here:
FilesDirsStartingWithCc = []

for (dirpath, dirnames, filenames) in subprocess.os.walk(CMEEwd):
    FilesDirsStartingWithCc += [subprocess.os.path.join(dirpath, file) \
        for file in filenames if file.startswith(("C", "c")) == True]

print(FilesDirsStartingWithCc)

#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

# Type your code here:
DirsStartingWithCc = []

for (dirpath, dirnames, filenames) in subprocess.os.walk(CMEEwd):
    DirsStartingWithCc += [subprocess.os.path.join(dirpath, dirname) \
        for dirname in dirnames if dirname.startswith(("C", "c")) == True]

print(DirsStartingWithCc)