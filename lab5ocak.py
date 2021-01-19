# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:40:44 2021

@author: Mehmed Emirhan AMAÇ-No:170420517
"""
import itertools
import time
def isPalindrome(a):
    for i in range(len(a)):
        if(a[i]!=a[len(a)-1-i]):
            return False
    return True
def stringecevir(last):
    last=str(last)
    last=last.replace(",", "")
    last=last.replace("[", "")
    last=last.replace("]", "")
    last=last.replace("'", "")
    last=last.replace(" ", "")
    last=last.replace("\n", "")
    return last
cumle=input("""En az 5 harfli kelime veya cumle giriniz:""")
cumle=cumle.lower()
cumle=cumle.replace(" ", "")
harfsayisi=len(cumle)
if (harfsayisi<5):
    print("Girilen ifade 5 harften az")
    time.sleep(1)
    exit()
cumleharf=list(cumle)
n=0
while(len(cumleharf)-n>=5):
    currentlist=list(itertools.combinations(cumleharf,len(cumleharf)-n))
    for i in range(len(currentlist)):
        if(isPalindrome(currentlist[i])):
            print(stringecevir(currentlist[i]))
    n=n+1