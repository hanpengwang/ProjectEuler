#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:14:31 2019

@author: hanpeng
"""

def primeFactor(n):
  mover = 2
  primes = []
  while mover<=n:
    if n%mover==0:
      primes.append(mover)
      n = n/mover
      mover = 2
    else:
      mover+=1
  return(primes)
    
  
def distinctPrimes(numOfPrimes, numOfConsec):
    n = 0
    
    while True:
        countPrime = 0
        for i in range(numOfConsec+1):
            num = n + i
            if len(set(primeFactor(num))) != numOfPrimes:
                break
            else:
                countPrime += 1
        
        if countPrime>=numOfConsec:
            break
        
        n += 1
        
    return n
            
        
    
print(distinctPrimes(4,4))

