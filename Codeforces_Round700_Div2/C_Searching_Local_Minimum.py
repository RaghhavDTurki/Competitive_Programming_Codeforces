#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:04:49 2021

@author: raghhav
"""
import sys
n = int(input())
maxn = 100010
a = [0] * (maxn)
a[0] = a[n+1] = n+1
l = 1; r = n;

def query(x):
    if ((1 <= x) and (x <= n)):
        print("? {}".format(x))
        sys.stdout.flush()
        a[x] = int(input())
        

while(l < r):
    m = (l+r) // 2
    query(m)
    query(m+1)
    if (a[m] < a[m+1]):
        r = m
    else:
        l = m+1
print("! {}".format(l))
sys.stdout.flush()
