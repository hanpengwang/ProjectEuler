#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:18:31 2020

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
  
  
  

def Goldbach_conjecture():
    
    p1 = 9
    while True:
        # p1 = p2 + 2 * s^2 where 1 <= s <= [(p1/2) - 1]^0.5 
        p1 += 2
        if len(primeFactor(p1)) != 0:
            found_prime = False 
            s = 1 
            boundary_s = int((p1/2 - 1)**0.5)
            while s < (boundary_s + 1): 
                p2 = p1 - 2 * s**2
                #print(s)
                if len(primeFactor(p2)) == 0:
                    found_prime = True
                    break
                s += 1
        else:
            found_prime = True
        
        
        if found_prime == False:
            return p1



print(Goldbach_conjecture())