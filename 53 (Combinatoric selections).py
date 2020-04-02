#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:52:53 2020

@author: hanpengwang
"""


from math import factorial as f

def Combinatoria_selections():
   
    count = 0
    
    for n in range(1,101):
        
        for r in range(1,n+1):
            
            if f(n)/(f(r)*f(n-r)) > 10**6:
                count +=1
                
    
    return count



print(Combinatoria_selections())