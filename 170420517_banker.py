# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:21:44 2022

@author: amacemirhan
Banker algoritmasi
Mehmed Emirhan Amaç - 170420517
"""
import numpy
# available = resource - sum(allocation)
resource = [10,5,7]
allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
Max = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
available=resource
available = numpy.asarray(available)#converting numpy array
resource = numpy.asarray(resource)
allocation = numpy.asarray(allocation)
Max = numpy.asarray(Max)
Need = Max-allocation
for i in allocation:
   available = available - i
print(available)
completed = numpy.array([])
a=[False,False,False,False,False]
itarate=0
while(a.count(True)!=5 and itarate<30):
    itarate += 1
    for i in range(5):
        comparison = available > Need[i]
        if a[i]:
            continue
        elif(comparison.all()):
            print("P",str(i),"      ")
            available += Max[i]
            a[i]=True
if (a.count(True)==5):
    print("deadlock olusmadi")
else:
    print("deadlock olustu. P",(a.index(False)),"  icin gerekenler ",str(Need[a.index(False)]-available))
    