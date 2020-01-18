#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:21:57 2020

@author: hanpeng
"""

     

      


def Double_base_palindromes():
    import numpy as np
    total = 0
    for i in range(10**6)[1:]:
        if list(str(i)) == list(str(i))[::-1]:
            if list(np.base_repr(i, base = 2)) == list(np.base_repr(i, base = 2))[::-1]:
                total += i 
    
    
    return total



print(Double_base_palindromes())
