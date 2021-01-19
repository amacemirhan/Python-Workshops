# -*- coding: utf-8 -*-
#odev-2.1
kelime="algoritma"
print("orijinal kelime:",kelime)
kelimeortasi=int(len(kelime)/2)
print("kelimenin ortasina ait index",kelimeortasi)
ortauc=""
for i in range(len(kelime)-1):
    if(i==kelimeortasi-1 or i==kelimeortasi or i==kelimeortasi+1):
        ortauc+=kelime[i]
print("kelimenin ortasina ait uc harf:",ortauc)
#odev-2.2
k1="Pembe"
k2="Yesil"
yenikelime=""
print("k1 kelimesi: ",k1)
print("k2 kelimesi: ",k2)
for i in range(len(k1)):
    if(i==0 or i==int(len(k1)/2) or i==len(k1)-1):
            yenikelime+=k1[i]
            yenikelime+=k2[i]
print("Yeni kelimemiz: ",yenikelime)