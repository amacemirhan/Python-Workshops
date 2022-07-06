# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:17:55 2021

@author: amacemirhan
"""
def Func():
    A=[3,8,2,6,1,10,17]
    N=len(A)
    mi=(N-1)/2.0
    swap=0
    for i in range(N):
        j=i
        for j in range(N-1):
            if(A[j]>A[j+1]):
                swap=A[j+1]
                A[j+1]=A[j]
                A[j]=swap
    if(mi%1 == 0.5):
        print((A[int(mi)]+A[int(mi)+1])/2)
    else:
        print(A[int(mi)])

Func()