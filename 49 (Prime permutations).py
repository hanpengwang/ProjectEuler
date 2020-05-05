#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:26:20 2020

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



def Prime_perm():
    import itertools
    
    numbers = [x for x in range(1000,10000)]
    
    collect = []
    
    for n in numbers:
        digits = list(str(n))
        perms = set(itertools.permutations(digits))
        perms_l = list()
        for p in perms:
            num = 0
            for (i, digit) in enumerate(p):
                num += 10**i * int(digit)
            if num >= 1000:
                perms_l.append(num)
                numbers.remove(num)
        temp = []
        for p in perms_l:
            if primeFactor(p) == True:
                temp.append(p)
        
        perms_l = temp
        
        if len(perms_l) >= 3:
            perms_l = sorted(perms_l)
            len_perms = len(perms_l)
            for (i,p) in enumerate(perms_l):

                for (i2,p2) in enumerate(perms_l[i+2:]):
                    
                    diff = p2 - p 
                    
                    if diff%2==0:
                        half = int(diff/2)
                        middle_num = p + half
                        if middle_num in perms_l[i+1:i2+i+2]:
                            collect.append([middle_num-half, middle_num, middle_num+half])
                    
    
    print(collect)
            
            
        
        
    
Prime_perm()