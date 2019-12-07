#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 01:12:46 2019

@author: hanpeng
"""

def lexicographicPermutations(l):
    import itertools 
    permList = [(''.join(str(n) for n in i)) for i in itertools.permutations(l)]
    #sorted(permList)
    return permList[10**6-1]


print(lexicographicPermutations([0,1,2,3,4,5,6,7,8,9]))