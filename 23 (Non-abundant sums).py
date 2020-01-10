#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:37:23 2019

@author: hanpeng
"""



def checkAbundant(num):
    divisors = [1]
    
    ## get divisors 
    for i in range((int(num**0.5)+1))[2:]:
        if num % i == 0:
            divisors.append(i)
            divisors.append(num//i)
    
    try:
        if divisors[-1] == divisors[-2]:
            divisors.pop()
    except:
        pass
    
    if sum(divisors) > num:
        return True
    
    return False
    

def NonAbundantSums():
    abundants = []
    sum_abundants = []
    for i in range(28124)[12:]:
        if_abundant = checkAbundant(i)
        if if_abundant:
            abundants.append(i)
    
    for a1 in abundants:
        for a2 in abundants:
            two_a_sum = a1 + a2
            if two_a_sum <= 28123:
                sum_abundants.append(a1 + a2)
    
    sum_abundants = set(sum_abundants)
    
    return (((1 + 28123) * 28123) / 2 - sum(sum_abundants)  )
   


print(NonAbundantSums())
