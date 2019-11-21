#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:49:56 2019

@author: hanpeng
"""

def Roots(a,b,c):
    part1 = -b / (2*a)
    part2 = (b**2 - 4*a*c)**0.5 / (2*a) 
    x1 = (part1 + part2)
    #x2 = int(part1 - part2) 
    return (x1)



def TPH():
    start = 286
    num = 0
    while True:
        T = (start ** 2 + start)/2 
        P_root = Roots(3, -1, -T*2)
        H_root = Roots(2, -1, -T)
        if str(P_root)[-1] == "0" and str(H_root)[-1] == "0":
            num = T 
            break
        
        start +=1 
    
    return num 
        
        
        
print(TPH())