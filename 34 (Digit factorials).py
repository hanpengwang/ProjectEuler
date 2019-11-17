#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:38:27 2019

@author: hanpeng
"""

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    
    
def numProcessor(n):
    return sum([factorial(int(i)) for i in str(n)]) 



def digitFactorials():
    upperBoundNum = 9999999 #[9,9,9,9,9,9,9]
    
    #update Bound 
    '''
    while True:
        for i in len(upperBoundDigits):
            while upperBoundDigits[i] > 1:
                upperBoundDigits[i] = upperBoundDigits[i] - 1  
            
            '''
    total = 0
    while upperBoundNum > 2:
        if numProcessor(upperBoundNum) == upperBoundNum:
            total += upperBoundNum
            print(upperBoundNum)
        upperBoundNum -= 1 
        
    return total 


print(digitFactorials())