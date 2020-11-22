#!/usr/bin/env python3

"""
Script illustrates the use of profiling on three functions
my_squares(iters) squares the input by the number of iters (iterations)
my_join(iters, string) joins the strings together by number of iters
run_my_funcs(x, y) runs the other two functions
"""

__appname__ = '[profileme.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

def my_squares(iters):
    """
    squares the input by the number of iters (iterations) using a for loop

    Parameters:
        iters (int): number of iterations
    
    Returns:
        out (list): list of squared iters
    """
    out = []
    for i in range(iters):
        out.append(i ** 2)
    return out

def my_join(iters, string):
    """
    joins the strings together by number of iters using join() and a for loop

    Parameters:
        iters (int): number of iterations
        string (str): given string

    Returns:
        out (str): concatenated string from input
    """
    out = ''
    for i in range(iters):
        out += string.join(", ")
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