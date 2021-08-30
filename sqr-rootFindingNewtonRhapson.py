#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:59:17 2021

@author: rachel
"""


# Python3 code for implementation of Newton
# Raphson Method for solving equations

# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
def func2( x, CS ):
    A = CS[0]
    B = CS[1]
    return x * x  + B*x + A

# Derivative of the above function
# which is 3*x^x - 2*x
def derivFunc2( x, CS ):
    A = CS[0]
    B = CS[1]
    return 2 * x + B

# Function to find the root
def newtonRaphson2( x, CS ):
    CS = CS
    h = func2(x, CS) / derivFunc2(x, CS)
    while abs(h) >= 0.0001:
        h = func2(x, CS)/derivFunc2(x, CS)
        x = x - h
    return x

# Driver program to test above

def rootFinder2(guess, CS):
    CS = CS
    x0 = guess # Initial values assumed
    r1 = newtonRaphson2(x0, CS)
    r2 = CS[2] - r1
    return r1,r2

R1, R2 = rootFinder2(guess = 2, CS = CS)

# This code is contributed by "Sharad_Bhardwaj"
