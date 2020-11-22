#!/usr/bin/env python3

"""
Script illustrates the use of numerical integration to solve the Lotka-Volterra 
model

The Lotka-Volterra model models predator-prey systems in a 2D space
dR/dt = -zC + eaCR
dC/dt = rR - aCR
R and C are resource and consumer densities 
r is the intrinsic (per-capita) growth rate of the resource
a is the per-capita "search rate" for the resource (area x time ^ -1) multiplied
  by its attack success probability, which determines the encounter and 
  consumption rate of the consumer on the resource
z is the mortality rate (time ^ -1)
e is the consumer's efficiency (a fraction) in converting resource to consumer 
  biomass
"""

__appname__ = '[LV1.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

# imports
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as p
import sys

# functions
def dCR_dt(pops, t = 0):
    """
    Growth rate of consumer and resource population at any given time step

    Parameters:
        pops (array): density of resource and consumer at time t
        t      (int): time step
    Return:
        sc.array([dRdt, dCdt]) : array containing the growth rate of resource 
                                 and consumer populations
    """
    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C
    dCdt = -z * C + e * a * R * C

    return np.array([dRdt, dCdt])

# assign parameter values
r = 1.0
a = 0.1
z = 1.5
e = 0.75

# define time vector, integrate from time point 0 to 15, using 1000
# sub-divisions of time
# note that units of time are arbitrary here
t = np.linspace(0, 15, 1000)

# set initial conditions for two populations (10 resources and 5 consumers per 
# unit area), and convert the two into an array (because our dCR_dt function
# takes an array as input)
R0 = 10
C0 = 5
RC0 = np.array([R0, C0])

def main():
    """
    Solves the Lotka-Volterra model by numerical integration
    Plots the results in two graphs saved to ../Results/. 
    First, a change in resource and consumer density over time, and second, the 
    change in population density of consumer with respect to the change in 
    population density of resource
    """

    # numerically integrate this system forward from those starting conditions
    # pops contains the results (the population trajectories)
    # infodict is a dictionary containing information on the integration
    pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output = True)
    type(infodict)
    infodict.keys()
    # check if integration was successful
    infodict["message"]

    # visualize with matplotlib
    f1 = p.figure()
    p.plot(t, pops[:,0], 'g-', label = "Resource density") # plot
    p.plot(t, pops[:,1], 'b-', label = "Consumer density")
    p.grid()
    p.legend(loc = "best")
    p.xlabel("Time")
    p.ylabel("Population density")
    p.title("Consumer-Resource population dynamics")
    # p.show()
    f1.savefig("../Results/LV_model.pdf") # save figure

    # plot of Consumer density against Resource density
    f2 = p.figure()
    p.plot(pops[:,0], pops[:,1], 'r-')
    p.grid()
    p.xlabel("Resource density")
    p.ylabel("Consumer density")
    p.title("Consumer-Resource population dynamics")
    # p.show()
    f2.savefig("../Results/LV_model1-1.pdf")

if __name__ == "__main__":
    main()
    sys.exit()