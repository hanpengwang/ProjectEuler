#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:03:41 2020

@author: hanpengwang
"""



def binet(n):
    phi =  2
    psi =  4
    return int(phi**n ) 


phi = (1 + 5**.5) / 2
psi = (1 - 5**.5) / 2

x = 2**10**15


def fib(n):
  
    v1, v2, v3 = 1, 1, 0  
    for rec in bin(n)[3:]:
        calc = (v2*v2) 
        v1, v2, v3 = (v1*v1+calc), ((v1+v3)*v2), (calc+v3*v3) 
        if rec == '1': v1, v2, v3 = (v1+v2), v1, v2
    return [v2,v1]  
    


def Quick_PolyFib(x,n,f1,f2):
    return int((-1 + x**n*f2 + x**(n+1)*f1) / (1+x-1/x))



def Poly_fib():
    n = 10**15
    f1, f2 = fib(n)
    
    total = 0
    
    for x in range(1,101):
        total += Quick_PolyFib(x, n, f1, f2)
    
    
    return total % 1307674368000
  





#print(Poly_fib())