#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:22:36 2019

@author: hanpeng
"""


def diophatineEquation():
    ## x^2 - 1 = Dy^2
    Max = 0
    D = 0
    for d in range(1001)[1:]:
        print(d)
        if str(d ** 0.5)[-1] != '0': 

            squarer = 1
            while True:
                x = (d * squarer**2 + 1)**0.5
                if str(x)[-1] == '0':
                    if x>Max:
                        Max = x
                        D = d
                    break
                    
                squarer += 1

    return [D, Max]

print(diophatineEquation())



