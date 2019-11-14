#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:33:31 2019

@author: hanpeng
"""

def factorial(n):
    
    if n == 1:
        return 1
    else:
        n -= 1 
        return (n+1) * factorial(n)
    
print(sum([int(i) for i in str(factorial(100))]))

    