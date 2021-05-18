# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:59:59 2019

@author: Snow
"""
import sys
stdout = sys.stdout
def sol(l):
    t=0
    for i in l:
        d=max(l)-i
        t=t+d
    return t
    


t=int(input())
for s in range(t):
    liste = []
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    from itertools import combinations
    for i in tuple(combinations(A, L)):
        liste.append(sol(i))
    print ("Case #%d: %d" % (s+1, int(min(liste))))
    stdout.flush()
        
