#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:21:10 2021

@author: raghhav
"""
t = int(input())
f = []
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    c0 = 0
    c1 = 0
    c2 = 0
    for i in a:
        if (i % 3) == 0:
            c0 += 1
        elif (i % 3) == 1:
            c1 += 1
        elif (i % 3) == 2:
            c2 += 1
    r = [c0,c1,c2]
    s = 0
    while(not((c1 == c2) and (c2 == c0))):
        for j in range(3):
            if (r[j] > n/3):
                r[j] -= 1
                r[(j+1) % 3] += 1
                if(j == 0):
                    c0 -= 1
                    c1 += 1
                elif(j == 1):
                    c1 -= 1
                    c2 += 1
                else:
                    c2 -= 1
                    c0 += 1
                s += 1
            else:
                pass
    f.append(s)
for k in f:
    print(k)