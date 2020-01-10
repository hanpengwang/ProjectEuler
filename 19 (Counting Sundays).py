#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:53:48 2019

@author: hanpeng
"""




countFeb29 = 0

monthDays = [31,[28,29],31,30,31,30,31,31,30,31,30,31]

firstDay = 2
countSunday = 0

for year in range(2001)[1901:]:
    for index, days in enumerate(monthDays):
        if index == 1:
            if year % 4 ==0:
                days = days[1]
            else:
                days = days[0]
                
        remainder = days % 7
        firstDay += remainder
        
        if firstDay % 7 == 0:
            countSunday+=1
            print(year,index)
        