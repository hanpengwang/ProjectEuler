#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:18:08 2020

@author: hanpeng
"""

def Champernowne_constant():
    concat = ""
    for i in range(1, 500000):
        concat += str(i)
    
    return int(concat[0]) * int(concat[9]) * int(concat[99]) * int(concat[999]) * int(concat[9999]) * int(concat[99999]) * int(concat[999999]) 


print(Champernowne_constant())