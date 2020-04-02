#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:43:10 2020

@author: hanpengwang
"""


def minSum(matrix):
    
    for i in range(len(matrix[0]))[1:]:
        matrix[0][i] = matrix[0][i] + matrix[0][i-1]
        
    for i in range(len(matrix))[1:]:
        matrix[i][0] = matrix[i][0] + matrix[i-1][0]
        
    for i in range(len(matrix))[1:]:
        for i2 in range(len(matrix[0]))[1:]:
            matrix[i][i2] = min(matrix[i][i2-1], matrix[i-1][i2]) + matrix[i][i2]
    
    return matrix[-1][-1]
    
    
        

file = open("/Users/hanpengwang/Downloads/p081_matrix.txt")
matrix = []
for i in file:
    matrix.append(list(map(int, i.split(","))))


print(minSum(matrix))


