#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:02:03 2019

@author: hanpeng
"""

def fifthPower(n):
    return sum([int(i)**5 for i in str(n)])



def digitFifthPower():
    
    upperBound = 9**5*6
    total = 0
    while upperBound > 2:
        if upperBound == fifthPower(upperBound):
            total += upperBound
        
        upperBound -= 1
        
    return total

print(digitFifthPower())
    