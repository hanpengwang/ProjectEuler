#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:01:31 2020

@author: hanpengwang
"""


def Digit_sum():
    ans = 0
    for a in range(1,100):
        for b in range(1,100):
            ans = max(ans,sum(list(map(lambda x:int(x),list(str(a**b))))))
    
    return ans


print(Digit_sum())