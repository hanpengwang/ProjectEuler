#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:42:58 2019

@author: hanpeng
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    
    
    
def latticePaths(n):
    return factorial(n*2) / (factorial(n)**2)


print(int(latticePaths(20)))