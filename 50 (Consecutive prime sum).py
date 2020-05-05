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


def Cons_prime():
    num = 0
    prime_test = 2
    while num <
    


