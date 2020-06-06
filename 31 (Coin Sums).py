#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:49:42 2019

@author: hanpeng
"""






def coinSums(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    arr = [1] + [0]*n
    for coin in coins:
        for i in range(coin, n+1):
            arr[i] += arr[i-coin]

    print(arr[-1])


coinSums(200)