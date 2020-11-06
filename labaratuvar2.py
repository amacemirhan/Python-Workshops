# -*- coding: utf-8 -*-
dize=input("Palindrom olup olmadigini kontrol etmek istediginiz dizeyi yaziniz:")
dize=dize.upper()
kontrol=1
for i in range(len(dize)-1):
    if (dize[i]!=dize[len(dize)-i-1]):
        kontrol=0
if (kontrol==1):
    print("Dize palindrom")
else:
    print("Dize palindrom değil")
