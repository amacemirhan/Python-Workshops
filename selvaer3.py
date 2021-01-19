# -*- coding: utf-8 -*-
import string
#Odev-3.1
def sayi_analizi():
    sayi=int(input("Input : "))
    if(sayi%2==0):
        print("Analiz 1: cift")
    else:
        print("Analiz 1: tek")
    if(sayi==0):
        print("Analiz 2: sifir")
    elif(sayi>0):
        print("Analiz 2: pozitif")
    else:
        print("Analiz 2: negatif")
    if(sayi<200 and sayi>-200):
        print("Analiz 3: inclusive")
    else:
        print("Analiz 3: exclusive")
sayi_analizi()
#Odev-3.2
def money_unit(data):
    index=data.find(" ")
    deger=int(data[0:index])
    data=data.title()
    if(data[index+1]=="T"):
        return (str(deger*0.13)+" Dolar")
    elif(data[index+1]=="D"):
        return (str(deger*7.84)+" Turk Lirasi")
    elif(data[index+1]=="P"):
        return (str(deger*1.12)+" Euro")
    elif(data[index+1]=="E"):
        return (str(deger*0.89)+" Pound")
    else:
        return ("Yanlis donusum girdiniz.")
print(money_unit("3 Turk Lirasi"))
print(money_unit("10 Pound"))
#Odev-3.3
def new_number(sayi):
    sayicpy=sayi
    sayi=str(sayi)
    sayi=list(sayi)
    sayi.sort()
    sayi.reverse()
    biggest_number=""
    for i in sayi:
        biggest_number+=i
    if(sayicpy==int(biggest_number)):
        print("Sayinin siralamasi degismedi")
    else:
        print(biggest_number)
new_number(318)
new_number(288)
new_number(333)