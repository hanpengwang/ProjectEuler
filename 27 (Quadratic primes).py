#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:14:43 2019

@author: hanpeng
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
  return(primes)
  
def quadraticPrimes(limit_a, limit_b):
    formular = lambda n, a, b : n**2 - a * n + b

    maxPrimes = 0
    maxProduct = 0
    
    for a in range(limit_a-1, -limit_a, -1):
        for b in range(limit_b, (-limit_b-1), -1):
            n = 0
            if formular(n, a, b) < 1:
                break
            
            while formular(n, a, b) >1 and len(primeFactor(formular(n, a, b))) == 0:
                n+=1

            if n > maxPrimes:
                maxPrimes = n
                maxProduct = - a * b

                
            
            
    return ([maxPrimes, maxProduct])


print(quadraticPrimes(100, 2000))

            
        
