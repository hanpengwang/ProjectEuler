#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:05:33 2019

@author: hanpeng
"""

def countDivisors(num):
    numSquare = int(num ** 0.5)
    count = 2
    for i in range(numSquare+1)[2:]:
        if num % i == 0:
            count += 2
    if i**2 == num:
        count -= 1 
    
    return count


def triNum(Min_divisors):
    Num = 3
    mover = 3
    while True:    
        Num += mover
        numDivisors = countDivisors(Num)
        if numDivisors >= Min_divisors:
            break
        mover += 1
        
        
    return Num

print(triNum(500))
