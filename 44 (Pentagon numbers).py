#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:44:38 2020

@author: hanpeng
"""

from math import sqrt

def Check_pen(N):
    ##complete rhs equation square and get this 
    n = 1/6 + sqrt((2*N+1/12)/3)
    return True if abs(n - round(n)) < 10**-4 else False



def Generate_pen(n):
    return n*(3*n - 1) / 2



def Pentagon_numbers():
    
    MIN = 10 ** 10
    #set an upper bound to trick the question
    for i1 in range(1,10**4):
        p1 = Generate_pen(i1)
        
        for i2 in range(i1+1,10**4):
            p2 = Generate_pen(i2)
            SUM = p1 + p2
            DIFF = p2 - p1 
            if Check_pen(SUM) and Check_pen(DIFF):
                MIN = min(MIN,DIFF)
                
    
    
    return MIN
                


print(Pentagon_numbers())


    
    

