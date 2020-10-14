# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: cfexercises1.py
# Desc: control flow tools
# Arguments:
# Date: Oct 2020

# What does each of foo_x do?
def foo_1(x):
    return x ** 0.5
# multiply x by 0.5 / square root x

def foo_2(x, y):
    if x > y:
        return x
    return y
# returns x if x > y, else return y

def foo_3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
        # could try x, y = y, x
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]
# rearranges x, y, z in ascending order

def foo_4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result
# returns product of 1 up to x+1

def foo_5(x): # A recursive function that calculates the factorial of x
    if x == 1:
        return 1
    return x * foo_5(x-1)

def foo_6(x): # Calculate the factorial of x in a different way
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto