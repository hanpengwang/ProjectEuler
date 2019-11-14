#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:53:47 2019

@author: hanpeng
"""

def Collatz(limit):
    Max = 0
    MaxNum = 0
    for i in range(limit,0,-1):
        thisNum = i
        count = 1
        while True:
            if i % 2 == 0:
                i /= 2
                count+=1
            else:
                i = i*3+1
                count+=1
            if i == 1:
                if count > Max:
                    Max = count
                    MaxNum = thisNum
                break
            
        

  
    return MaxNum
        
        

print(Collatz(10**6))
    