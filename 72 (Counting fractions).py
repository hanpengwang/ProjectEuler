#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:30:50 2020

@author: hanpengwang
"""


def primeFactors(n): 
    primes = []
    while n % 2 == 0: 
        primes.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(n**0.5)+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            primes.append(int(i))
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        primes.append(int(n))
        
    
    return set(primes)

def Count_fractions():
    
    ## for 1 to 10**6; get each n prime factors and save to dictionary according to prime factors as key, and save it as in order ,second interation going through each number to find numbers with common prime factors then exclude them for this number  
    return 0



print(primeFactors(10000))