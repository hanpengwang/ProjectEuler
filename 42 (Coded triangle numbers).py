#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:26:40 2020

@author: hanpengwang
"""

def CodedTri_num():
    from math import sqrt
    d = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,
         "g":7,"h":8,"i":9,"j":10,"k":11,"l":12,
         "m":13,"n":14,"o":15,"p":16, 
         "q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23, 
         "x":24,"y":25,"z":26}
    
    for k in list(dict.keys(d)):
        d[str.upper(k)] = d.pop(k)
        
    f = open("/Users/hanpengwang/Downloads/p042_words.txt", "r")
    words = f.read().split(",")
    COUNT = 0
    for w in words:
        w = w[1:-1]
        count = 0
        for alpha in w:
            count += d[alpha]
        #complete square for tri equation
        if abs(round(sqrt(2*count+1/4)-1/2) - (sqrt(2*count+1/4)-1/2)) < 10**(-4):
            COUNT += 1
    
    return COUNT
    
print(CodedTri_num())