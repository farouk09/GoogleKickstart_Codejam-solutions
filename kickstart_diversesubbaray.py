# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 00:20:14 2019

@author: Snow
"""

t=int(input())
for s in range(t):
    k=0 
    N, S = map(int, input().split())
    A = list(input())
    for i,j in enumerate(A):
        if A.count(j)>S:
            dec=A.count(j)
            for k in range(dec):
               A[i+1]=j
               p=p+1
               if
            
            
            
   
                
    print ("Case #%d: %d" % (s+1, Q-k))     