# Author: Yewshen Lim y.lim20@imperial.ac.uk
# Script: cfexercises2.py
# Desc: loops and conditionals combined
# Arguments:
# Date: Oct 2020

for j in range(12):
    if j % 3 == 0:
        print('hello')
# prints 4 hellos

for j in range(15):
    if j % 5 == 3:
        print('hello')
    elif j % 4 == 3:
        print('hello')
# prints 5 hellos

z = 0
while z != 15:
    print('hello')
    z = z + 3
# prints 5 hellos

z = 12
while z < 100:
    if z == 31:
        for k in range(7):
            print('hello')
    elif z == 18:
        print('hello')
    z = z + 1
# prints 8 hellos