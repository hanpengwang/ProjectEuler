#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:14:43 2019

@author: hanpeng
"""


from decimal import *

def Reciprocal_cycles():

    getcontext().prec = 1000
    
    max_rec = 1
    max_rec_num = 0
    
    for d in range(1001)[2:]:
        decimals = list((Decimal(1)/Decimal(d)).as_tuple().digits)
        if len(decimals) == 1000:
            for i in range(501)[1:]:
                multiplier = len(decimals) // i
                sum_decimals = sum(decimals[0:(multiplier * i)])
                sum_interval = sum(decimals[0:i])
                if sum_decimals == sum_interval * multiplier:
                    #print(i,d)
                    if i > max_rec:
                        max_rec = i 
                        max_rec_num = d
                    break
        
    
    print({max_rec_num: max_rec})
            
        
        
Reciprocal_cycles()
 ### method: slice a interval(from 1 to inf) from first element in the list, check equality of sum(interval)*len(list)/len(interval) == sum(interval) 
        
        
    
    