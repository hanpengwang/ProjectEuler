#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:59:35 2019

@author: hanpeng
"""

def selfPowers(limit):
    count = 0
    
    for i in range(limit+1)[1:]:
        count += i**i
    
    digits = [i for i in str(count)]
    
    return "".join(digits[-10:])


print(selfPowers(1000))
