#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:21:29 2020

@author: hanpeng
"""


def Find_pandigital(num):

    for i in range((int(num**0.5)+1))[2:]:
        if num % i == 0:
            list_nums = list(map(lambda x:int(x),list(str(i)) + list(str(num//i)) + list(str(num))))

            if len(list_nums) == 9:
                if sum(list_nums) == 45 and reduce(lambda a,b:a*b, set(list_nums)) == 362880:
                    print(sorted(list_nums))
                    return True
    
    return False


def Pandigital_produtcs():
    from functools import reduce
    total = 0
    for product in range(9999):
        if Find_pandigital(product):
            total+=product
            
            
    return total


print(Pandigital_produtcs())
            
            


    
    