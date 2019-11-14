#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:42:15 2019

@author: hanpeng
"""

def sumDivisors(num):
    numSquare = int(num ** 0.5)
    count = 1
    placeholder = 0
    for i in range(numSquare+1)[2:]:
        if num % i == 0:
            count += i
            count += num/i
            placeholder = i
    if placeholder**2 == num:
        count -= placeholder
    
    return int(count)

def amicableNumber(limit):
    
    start = 50
    count = 0
    for i in range(limit+1)[start:]:
        n1 = sumDivisors(i)
        n2 = sumDivisors(n1)
        if n2 == i and n2 < limit and i!=n1:
            count += i
 
            
    return count 

print(amicableNumber(10000))
    