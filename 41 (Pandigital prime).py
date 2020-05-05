#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:51:04 2020

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



def Pan_prime():
    import itertools
    numbers = [x for x in range(1,8)]
    
    perms = set(itertools.permutations(numbers))
    perms_l = list()
    for p in perms:
        num = 0
        for (i, digit) in enumerate(p[::-1]):
            num += 10**i * int(digit)
        
        if num%2 == 1:
            perms_l.append(num)
            
    perms_l = sorted(perms_l,reverse=True)
    
    for p in perms_l:
        if primeFactor(p):
            print(p)
            return p
    
Pan_prime()