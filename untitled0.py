# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:07:28 2021

@author: amacemirhan
"""
A=[1,2,3,4,5,6,7,8,9,8,7,4,5,7,8,8,7,7,7]
B =[]
say = 0
top=0
maax=0
maaxeleman=0
for i in range(len(A)):#n
    j=i
    for j in range(len(A)):#n
        top=top+1
        if A[i]==A[j]:
            say = say+1
    
    B.append([A[i],say])
    say=0
    if (B[i][1]>maax):
        maax=B[i][1]
        maaxeleman=B[i][0]
        
   
print(B)   
print(top)
print(maaxeleman)

    
    