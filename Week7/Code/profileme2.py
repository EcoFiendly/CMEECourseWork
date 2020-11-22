#!/usr/bin/env python3

"""
Script profiles the vectorized versions of my_squares and my_join from 
profileme.py
"""

__appname__ = '[profileme2.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

def my_squares(iters):
    """
    squares the input by the number of iters (iterations) using list 
    comprehension

    Parameters:
        iters (int): number of iterations

    Returns:
        out (list): list of squared iters
    """
    out = [i ** 2 for i in range(iters)]
    return out

def my_join(iters, string):
    """
    joins the strings together by number of iters using += and a for loop

    Parameters:
        iters (int): number of iterations
        string (str): given string

    Returns:
        out (str): concatenated string from input
    """
    out = ''
    for i in range(iters):
        out += ", " + string
    return out

def run_my_funcs(x, y):
    """
    runs my_squares and my_join

    Parameters:
        x (int): number of iterations
        y (str): given string
    
    Returns:
        prints inputs
        prints output of my_squares and my_join
    """
    print(x, y)
    my_squares(x)
    my_join(x, y)
    return 0

run_my_funcs(10000000, "My string")