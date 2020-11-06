# -*- coding: utf-8 -*-
num=int(input("tam sayi giriniz:"))
if (num<0):
    print("Thanks for playing along!")
    exit()
# elif (num/10==0):
#     print("For the integer:",num)
#     print("Additive Persistence=0, Additive Root=",num)
#     print("Multiplicative Persistance=0, Multiplicative Root="num)
else:
    sayac=0
    top=0
    num2=num
    print("For the integer: ",num)
    print("Addition")
    while ((int)(num/10)!=0):
        top = top+num%10
        num=num/10
        num=int(num)
        if((int)(num/10)<0):
            num=top
            print("New Value:",num)
            sayac=sayac+1
        
    print("Additive Persistence=",sayac," Additive Root=",num)
    sayac=0
    top=1
    print("Multiplication")
    while ((int)(num2/10)!=0):
        top = top*num2%10
        num2=num2/10
        num2=int(num2)
        if((int)(num2/10)<0):
            num2=top
            print("New Value:",num2)
            sayac=sayac+1
    print("Multiplicative Persistance=",sayac," Multiplicative Root=",num2)
    