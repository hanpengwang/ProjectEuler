#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:31:33 2020

@author: hanpengwang
"""


def digitCanc():
    upper = 1
    lower = 1
    
    for denominator in range(11,100):
        
        for numerator in range(10, denominator):
            
            str_denom = list(str(denominator))
            str_num = list(str(numerator))
            
            for digit in str_denom:
                if digit in str_num:
                    str_num.remove(digit)
                    str_denom.remove(digit)
                    
                
                    digit = int(digit)
                    
                    if digit == 0:
                        digit = 10
                    
                    if denominator % digit != 0 and numerator % digit !=0:
                        if numerator/denominator == int(str_num[0])/int(str_denom[0]):
                            #curious.append([numerator,denominator])
                            upper = upper * int(str_num[0])
                            lower = lower * int(str_denom[0])
                          
                    
                    break
    
    return lower/upper


print(digitCanc())