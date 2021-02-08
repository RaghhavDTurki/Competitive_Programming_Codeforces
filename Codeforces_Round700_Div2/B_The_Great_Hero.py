#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:46:08 2021

@author: raghhav
"""

import math
t = int(input())
f = []
for _ in range(t):
    A,B,n = [int(x) for x in input().split()]
    a  = [int(x) for x in input().split()]
    b =  [int(x) for x in input().split()]
    term = 0
    for j in range(0,n):
        q = math.ceil(b[j]/A)
        t = q * a[j]
        term += t
    counter = 0
    while counter < n:
        if (counter != n-1):
            if ((B - term + a[counter]) > 0):
                f.append("YES")
                break
            else:
                pass
        else:
            if ((B - term + a[counter]) > 0):
                f.append("YES")
                break
            else:
                f.append("NO")
                break
        counter+= 1
        
for k in f:
    print(k)