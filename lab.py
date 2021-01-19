# -*- coding: utf-8 -*-
#Mehmed Emirhan Amac - 170420517
import time
nameoff=input("Dosya adini girin:")
try:
    dosya = open(nameoff,"r+")
except FileNotFoundError:
    print("Dosya Bulunamadı!")
    time.sleep(0.5)
    exit()
veri=dosya.read()
veriler=veri.split(" ")
print("Dosyadan ",len(veriler)," adet deger okundu")
print("Listenin ilk hali:\n",veri)

try:
    maxd=int(input("Max degeri girin:"))
except ValueError:
    print("Lutfen tamsayi giriniz")
    time.sleep(0.5)
    exit()
def change(maks,data,index):#recursive
    if(index==len(data)):
        return True
    elif(int(data[index])>maks):
        data[index]=maks
    return change(maks, data, index+1)
n=0
for i in range(len(veriler)):
    if(int(veriler[i])>maxd):
        n=n+1
change(maxd, veriler, 0)
print(n," deger max yapildi")
print("Listenin son hali:")
dosya.write("\nDeğistirilmis veriler:\n")
last=str(veriler)
for i in (veriler):
    print(i," ",end="")
last=last.replace(",", "")
last=last.replace("[", "")
last=last.replace("]", "")
last=last.replace("'", "")
last=last.replace("\n", "")
print("Dosyaya yeni veriler yazildi")
dosya.write(last)
dosya.close()

