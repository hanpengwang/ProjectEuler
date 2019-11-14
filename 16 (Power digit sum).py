#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:20:56 2019

@author: hanpeng
"""

def powerDigitSum(base, power):
    num = base ** power
    numDigits = [int(i) for i in str(num)]
    return sum(numDigits)


print(powerDigitSum(2,1000))
    