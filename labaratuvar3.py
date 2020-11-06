# -*- coding: utf-8 -*-
import random
liste = [] #liste olusturdum icindeki degerleri degistiricem
for i in range(20):
    liste.append(random.randint(1,100))
print(liste)
top=0
ort=0.0
for j in range(0,len(liste)-1):
    top+=liste[j]
ort=top/len(liste)
print(ort)
liste.sort()
print("largest value=",liste[len(liste)-1],",smallest value=",liste[0])
print("2.largest value=",liste[len(liste)-2],",2.smallest value=",liste[1])
say=0
for d in liste:
    if (d%2==0):
        say=say+1
print("there are ",say," even numbers")
