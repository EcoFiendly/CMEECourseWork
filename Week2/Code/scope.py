# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: scope.py
# Desc: variable scope, local and global
# Arguments:
# Date: Oct 2020

"""
Variables inside functions are invisible outside of it, nor do they persist once
the function has run. These are called local variables, and are only accessible 
inside their function. However, "global variables are visible inside and outside
of functions.
"""

_a_global = 10 # a global variable

if _a_global >= 5:
    _b_global = _a_global + 5 # also a global variable

def a_function():
    _a_global = 5 # a local variable

    if _a_global >= 5:
        _b_global = _a_global + 5 # also a local variable

    _a_local = 4

    print("Inside the function, the value of _a_global is ", _a_global)
    print("Inside the function, the value of _b_global is ", _b_global)
    print("Inside the function, the value of _a_local is ", _a_local)

    return None # good practice to explicitly return None if no return specified

a_function()

print("Outside the function, the value of _a_global is ", _a_global)
print("Outside the function, the value of _b_global is ", _b_global)

_a_global = 10

def a_function():
    _a_local = 4

    print("Inside the function, the value of _a_local is ", _a_local)
    print("Inside the function, the value of _a_global is ", _a_global)

    return None

a_function()

print("Outside the function, the value of _a_global is ", _a_global)


# To modify or assign a global variable from inside a function, use "global"

_a_global = 10
print("Outside the function, the value of _a_global is", _a_global)

def a_function():
    global _a_global
    _a_global = 5
    _a_local = 4

    print("Inside the function, the value of _a_global is ", _a_global)
    print("Inside the function, the value of _a_local is ", _a_local)

    return None

a_function()

print("Outside the function, the value of _a_global now is ", _a_global)

# global keyword also works from inside nested functions, but it can be slightly
# confusing

def a_function():
    _a_global = 10

    def _a_function2():
        global _a_global
        _a_global = 20

    print("Before calling a_function, value of _a_global is ", _a_global)

    _a_function2()

    print("After calling _a_function2, value of _a_global is ", _a_global)

    return None

a_function()

print("The value of _a_global in main workspace / namespace is ", _a_global)

# Compare above with below

_a_global = 10

def a_function():

    def _a_function2():
        global _a_global
        _a_global = 20

    print("Before calling a_function, value of _a_global is ", _a_global)

    _a_function2()

    print("After calling _a_function2, value of _a_global is ", _a_global)

a_function()

print("The value of _a_global in main workspace / namespace is ", _a_global)