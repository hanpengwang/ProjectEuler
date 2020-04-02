#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:09:27 2020

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


def Spiral_primes():
    num = 1 
    base = 1
    prime = 0 
    step = 2
    ratio = 100
    side_len = 1
    while ratio>=0.1:
        print(ratio, len)
        side_len += 2
        for cycle in range(4):
            num += step
            base += 1
            if primeFactor(num):
                prime += 1
            else:
                ratio = prime / base
        step += 2 
       
        
    return side_len



print(Spiral_primes())
    
            
            
            
        
        
    


