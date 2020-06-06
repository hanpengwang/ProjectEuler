#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:14:43 2019

@author: hanpeng
"""


from math import log10

def reciprocalCycles():
    maxRec = 0
    maxNum = 0
    for i in range(2,1000):
        
        remainders = dict()
        multiplier = 1 
        while True:
           
            remainder = multiplier % i
            if remainder == 0:
                break 
            if multiplier == 1:
                remainders[remainder] = log10(multiplier)  #index
            else: 
                if remainder in remainders: 
                    recLength = log10(multiplier) - remainders[remainder] 
                    if recLength > maxRec:
                        maxNum = i
                        maxRec = recLength
                    break 
                else: 
                    remainders[remainder] = log10(multiplier)
            multiplier *= 10
    return maxNum



    

print(reciprocalCycles())
            
        
        
