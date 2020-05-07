#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:55:12 2020

@author: hanpengwang
"""


def SubString_div():

    from itertools import permutations 
    
    perm = permutations(["0","1", "2", "3","4","5","6","7","8","9"]) 
    perm = list(filter(lambda number: int("".join(number)) > 10**9, list(perm)))
    
    divisors = [2,3,5,7,11,13,17]
    SUM = 0
    for p in perm:
        for i in range(len(divisors)):
            d = divisors[i]
            subset = p[1+i: 4+i]
            if int("".join(subset)) % d != 0:
                break
            elif d == 17 and int("".join(subset)) % d == 0:
                SUM = SUM + int("".join(p))
    
    return SUM
        
    

print(SubString_div())
        
    
    
