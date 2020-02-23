#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:44:38 2020

@author: hanpeng
"""


def Check_pen(p):
    num = (2 * p + 1/12)**0.5 / 3**0.5 + 1/6
    return int(str(num).split(".")[1]) < 10

def Generate(n):
    return n*(3*n - 1) / 2

def Pentagon_numbers():
    l = []
    
    Min = 10**10
    
    for i in range(2*10**4)[1:]:
        l.append(int(Generate(i)))
    
    for p1 in l:
        for p2 in l[p1:]:
            if Check_pen(p1+p2) and Check_pen(p2-p1):
                print(p2-p1)
                Min = min(Min, (p2-p1))
                
                
    return Min

    
    

print(Pentagon_numbers())