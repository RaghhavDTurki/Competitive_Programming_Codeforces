#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:21:13 2021

@author: raghhav
"""
t = int(input()) 
f = []
for _ in range(t): 
    n = int(input())
    cubes = {}
    for i in range(1,int(n**(1./3.))+8): 
        cubes[i**3] = 1
    for i in range(1,len(cubes)): 
        a = i**3
        b = n - a
        if b in cubes: 
            ans = "YES"
            break
        else:
            ans = "NO"
    f.append(ans)
for k in f:
    print(k)