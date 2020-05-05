#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:40:48 2020

@author: hanpeng
"""

def Pandigital_multiples():
    MAX = 0
    number = 1 
    while True:
        pan = ""
        for n in range(1,10):
            pan = pan + str(number*n)
            if len(pan)>=9:
                break
        if len(pan) == 9 and sorted(list(pan)) == ["1","2","3","4","5","6","7","8","9"]:
            MAX = max(MAX, int(pan))
            
        if len(pan)>9 and n == 2:
            break
        
        number += 1
    return MAX
            
            

print(Pandigital_multiples())
