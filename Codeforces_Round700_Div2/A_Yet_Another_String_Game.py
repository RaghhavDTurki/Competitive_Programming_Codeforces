#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:43:47 2021

@author: raghhav
"""
t = int(input())
f = []
for _ in range(t):
    s = input()
    n = len(s)
    stol = []
    for k in s:
        stol.append(k)
    for i in range(n):
        if (i % 2 == 0):
            if (s[i] == 'a'):
                stol[i] = 'b'
            else:
                stol[i] = 'a'
        else:
            if (s[i] == 'z'):
                stol[i] = 'y'
            else:
                stol[i] = 'z'
    s1 = ''.join(map(str,stol))
    f.append(s1)
    
for j in f:
    print(j)