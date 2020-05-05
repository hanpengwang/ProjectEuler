#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:52:26 2020

@author: hanpengwang
"""


def Pow_counts():
    count = 1
    for base in range(2,10):
        power = 1
        while True:
            #print(count)
            result = base ** power 
           
            if len(str(result)) == power:
                count += 1
                print(result)
            elif len(str(result)) < power:
                break
            
            power += 1
    
    return count


print(Pow_counts())
           
        
               
           
        
            
            
        
    