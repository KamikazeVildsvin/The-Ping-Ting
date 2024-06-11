# functions for RC calculations

import numpy as np

def cutoff(r, c):
    return (1 / (2*np.pi*r*c))

def naturalFrequency(r, c):
    return (1 / (r*c))

def timeConstant(r, c):
    return r*c

def astablePeriod(r,c):
    return 2*r*c