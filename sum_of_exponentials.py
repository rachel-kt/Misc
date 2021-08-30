#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:52:52 2021

@author: rachel
"""
import numpy as np
from numpy.linalg import inv

#-------------------------------- test data ----------------------------------#
#'''
b=0.05
c=0.08
p=-0.005
q=-0.0001
x= np.arange(0,1000,0.3)

y = np.add(b*np.exp(np.multiply(p,x)),c*np.exp(np.multiply(q,x)))
#y = y+y*np.random.normal(0,0.02,len(x))
plt.plot(x,y)
#'''
#-----------------------------------------------------------------------------#
def fitSumOfExponentials(x,y):
    S = np.zeros(len(x))
    SS = np.zeros(len(x))
    S[0] = 0
    SS[0] = 0
    for k in np.arange(1,len(x)):
        S[k] = S[k-1] + 0.5*(y[k]+y[k-1])*(x[k]-x[k-1])
        SS[k] = SS[k-1] + 0.5*(S[k]+S[k-1])*(x[k]-x[k-1])
        
        
    M = np.zeros((4,4))
    M[0,0] = np.sum(np.square(SS))
    M[0,1] = np.sum(np.multiply(SS,S))
    M[1,0] = np.sum(np.multiply(SS,S))
    M[0,2] = np.sum(np.multiply(SS,x))
    M[2,0] = np.sum(np.multiply(SS,x))
    M[1,1] = np.sum(np.square(S))
    M[0,3] = np.sum(SS)
    M[3,0] = np.sum(SS)
    M[1,2] = np.sum(np.multiply(S,x))
    M[2,1] = np.sum(np.multiply(S,x))
    M[1,3] = np.sum(S)
    M[3,1] = np.sum(S)
    M[2,2] = np.sum(np.power(x,2))
    M[3,2] = np.sum(x)
    M[2,3] = np.sum(x)
    M[3,3] = len(y)
    
    Y = np.zeros((4))
    
    Y[0] = np.sum(np.multiply(SS,y))
    Y[1] = np.sum(np.multiply(S,y)) 
    Y[2] = np.sum(np.multiply(x,y)) 
    Y[3] = np.sum(y) 
    
    
    Minv = inv(M)
    CS = np.inner(Minv,Y)
    
    A = CS[0]
    B = CS[1]
    

    #R1, R2 = rootFinder2(guess = 0.005, CS = CS)
    p_result = round(0.5*(B + np.sqrt(abs(B*B+4*A))),8)
    q_result = round(0.5*(B - np.sqrt(abs(B*B+4*A))),8)
    
    
    Beta = np.exp(p_result*x)
    Eta = np.exp(q_result*x)
    
    # Beta = np.exp(-0.02*x)
    # Eta = np.exp(-0.001*x)
    
    N = np.zeros((2,2))
    
    N[0,0] = np.sum(np.square(Beta))
    N[0,1] = np.sum(np.multiply(Beta,Eta))
    N[1,0] = np.sum(np.multiply(Beta,Eta))
    N[1,1] = np.sum(np.square(Eta))
    
    YY = np.zeros((2))
    YY[0] = np.sum(np.multiply(Beta,y))
    YY[1] = np.sum(np.multiply(Eta,y))
    
    Ninv = inv(N)
    
    dS = np.inner(Ninv,YY)
    print(p_result, q_result, dS)

    return p_result, q_result, dS[0], dS[1]

a,b,c,d = fitSumOfExponentials(x, y)
CS = np.asarray([c,d])

y_exp = np.add(c*np.exp(np.multiply(a,x)), d*np.exp(np.multiply(b,x)))
plt.plot(y, label = "data")
plt.plot(y_exp, label = "calculated")
plt.legend()

#------------------------------ variance -------------------------------------#
