#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 02:00:01 2020

@author: hanpeng
"""


def Integer_right_triangles():
    max_count = 0
    max_p = 0 
    for p in range(10, 1000):
        p_count = 0
        if p%2 == 0:
            c_upper = p / 2 - 1
        else:
            c_upper = p // 2
        if p % 3 == 0 or p % 3 == 1:
            c_lower = p / 3 + 1
        else:
            c_lower = p / 3 + 2 
        for c in range(int(c_lower), int(c_upper) + 1):
            remainder = p - c 
            if remainder % 2 == 0: 
                start = int(remainder / 2) 
            else:
                start = int(remainder // 2) + 1 
            for a in range(start, c):
                b = remainder - a 
                if c**2 == a**2 + b**2:
                    p_count += 1
                    break 
        if p_count > max_count:
            max_p = p
            max_count = p_count

    return [max_p, max_count]

print(Integer_right_triangles())
