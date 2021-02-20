#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:45:38 2021

@author: raghhav
"""
import math
t = int(input())
f = []
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    for i in range(n-1):
        if (max(a[i],a[i+1])/min(a[i],a[i+1])) <= 2:
            pass
        else:
            x = (math.log((max(a[i],a[i+1])/min(a[i],a[i+1])),2))  
            if(x.is_integer()):
                count += int(x-1)
            else:
                count += int(x)
    f.append(count)
    
for j in f:
    print(j)