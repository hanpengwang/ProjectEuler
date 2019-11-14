#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:28:34 2019

@author: hanpeng
"""

def distinctPowers(a, b):
    collect = []
    for i in range(a+1)[2:]:
        
        for i2 in range(b+1)[2:]:
            collect.append(i**i2)
            
    return len(set(collect))



print(distinctPowers(100,100))