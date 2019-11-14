#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:16:42 2019

@author: hanpeng
"""

def MaximumPathSumII():
    file1 = open("/home/hanpeng/Downloads/numbers.txt")
    list_tri = []

    for i in file1:
        list_tri.append(list(map(int, i.split())))
    
    list_tri = [l[0] for l in list_tri]
    total = sum(list_tri)
    list_total = [digit for digit in str(total)]
    list_first10 = list_total[0:10]
    num = int("".join(list_first10))
    return num

num = MaximumPathSumII()