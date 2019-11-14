#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:22:47 2019

@author: hanpeng
"""

def numTransform(n):
    ones = ["one","two","three","four", "five", "six","seven","eight","nine","ten","eleven","twelve", "thirteen", "fourteen", "fifteen","sixteen","seventeen", "eighteen","nineteen"]
    tenth = ["twenty","thirty","forty", "fifty","sixty","seventy","eighty","ninety"]
 
    thousands = ["thousand"]
    
    ones = [len(i) for i in ones]
    tenth = [len(i) for i in tenth]
    thousands = [len(i) for i in thousands]
    
    90 * sum(ones[0:10]) + 10 * sum(ones[10:]) + 90 * sum(tenth) + 3 * 
    

    
 
 
    
    

