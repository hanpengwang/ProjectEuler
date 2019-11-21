#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:11:15 2019

@author: hanpeng
"""


def digitCheck(n):
    return sorted([i for i in str(n)])

def permutedMultiples():
    n = 1
    while True:
        if len(str(n)) < len(str(n*6)):
            n = 10**len(str(n))
        if digitCheck(n) == digitCheck(n*2) \
        == digitCheck(n*3) == digitCheck(n*4) \
        == digitCheck(n*5) == digitCheck(n*6):
            return n
        n+=1
            
        

print(permutedMultiples())

