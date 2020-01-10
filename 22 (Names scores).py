#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:46:32 2019

@author: hanpeng
"""



f = open("/home/hanpeng/ProjectEuler/22 (names).txt", "r")

nameList = sorted([name[1:-1] for name in f.readlines()[0].split(",")])


alphas = 'abcdefghijklmnopqrstuvwxyz'

helper_dict = {}

for index, a in enumerate(alphas):
    helper_dict[a] = index + 1
    

total = 0
for index, name in enumerate(nameList):
    count = 0
    for word in name:
        word = word.lower()
        count += helper_dict[word]
    
    total += count * (index + 1)
    
