#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:05:24 2020

@author: hanpengwang
"""

def primeFactor(n):

    mover = 2
    primes = []
    while mover<= n**0.5:
      if n%mover==0:
        primes.append(mover)
        n = n/mover
        mover = 2
      else:
        mover+=1
    return True if len(primes) == 0 else False


def Prime_gen():
    prime_l = []
    for n in range(2,10**4+1):
        if primeFactor(n):
            prime_l.append(n)
   
    return prime_l



def Con_prime_sum():
    prime_l = Prime_gen()
    count_len = 0 
    prime = 0
    
    for i in range(1,len(prime_l)+1):
        partial_l = prime_l[i:]
        len_partial = len(partial_l)
        if len_partial <= count_len:
            break
        
        for i2 in range(1, len_partial)[::-1]:
            subset = partial_l[1:i2+1]
            _sum = sum(subset)
            if _sum < 10**6 and primeFactor(_sum):
                if count_len < len(subset):
                    count_len = len(subset)
                    prime = _sum
                break
    
    return prime
    

print(Con_prime_sum())


