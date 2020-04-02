#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:07:19 2020

@author: hanpengwang
"""


def Lychrel_numbers():
    count = 0 
    for i in range(1,10000):
        i2 = i
        n = 0
        while n <55:
            i_reverse = int(str(i)[::-1])
            i += i_reverse
            
            if i == int(str(i)[::-1]):
                count += 1
                
                break
            
            n += 1
    
    return (9999 - count) 
            
    
        
        

print(Lychrel_numbers())