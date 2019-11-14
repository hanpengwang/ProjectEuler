#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:58:43 2019

@author: hanpeng
"""

def primeFactor(n):
  if n == 1:
      return 10
  mover = 2
  count = 0 
  while mover<=n**0.5:
    if n%mover==0:
      count +=1 
      n = n/mover
      mover = 2
    else:
      mover+=1
  return(count)
    
  


def truncatablePrimes():
    n = 11
    count = 0
    Sum = 0
    while True:
        innerCount = 0
        for i in range(len(str(n))):
            sliceRight = int(str(n)[i:])
            sliceleft = int(str(n)[:i+1])
            if primeFactor(sliceRight) !=0 or primeFactor(sliceleft) !=0:
                break
            else:
                innerCount+=1
        
        if innerCount == len(str(n)):
            print(n)
            count += 1
            Sum += n
        if count == 11:
            break
        
        n += 2
        
    return(Sum)
        
        
        
    

print(truncatablePrimes())