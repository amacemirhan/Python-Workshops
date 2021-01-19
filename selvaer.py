# -*- coding: utf-8 -*-
import math
#1.odev
cinsiyet="K"
boy=160
kilo=62
yas=18
bmh=0.0
if (cinsiyet=="K"):
    bmh=655+(9.6*kilo)+(1.8*boy)-(4.7*yas)
elif (cinsiyet=="E"):
    bmh=65.5+(13.7*kilo)+(5*boy)-(6.7*yas)
else:
    print("Yanlıs cinsiyet degeri girdiniz.")
bmh=round(bmh)
print("Bazal Metabolizma hiziniz",bmh)
#2.odev
nufus=330569135
#9-- 11++ 47++ =ekoku 4653 sn yede (-517+423+99) nufus 5 kişi artıyor
yil=int(input("Kac yil sonraki tahmini populasyon bulunsun:"))
popafteryrs=int(((yil*31556926)/4653)*5+nufus)
nufusartisi=popafteryrs-nufus
print(yil," yil gectikten sonraki tahmini nufus artisi",nufusartisi)
#3.odev
selvaer="""I thought a thought.
But the thought I thought
Wasn’t the thought I thought I thought.
If the thought I thought I thought,
Had been the thought I thought,
I wouldn’t have thought I thought."""
index=0
for i in range(10):
    index = selvaer.find("thought",index+1,len(selvaer)-1)
print("Onuncu thought kelimesinin indexi:",index)
#4.odev
h=5
s=10
r=math.pow(s*s-h*h,1/2)
print("Koninin yarıcapı ",r," cm dir.")
yuzeyalani=math.pi*r*(r+s)
print("Koninin yuzeyalani ",yuzeyalani," cm karedir.")
hacim=(math.pi*r*r*h)/3
print("Koninin hacmi ",hacim," cm kuptur.")


    


