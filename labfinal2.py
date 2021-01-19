# -*- coding: utf-8 -*-
numbers=[]
giris=""
while(giris!="quit"):
    giris=input("")
    if(giris!="quit"):
        try:
            numbers.append(int(giris))
        except ValueError:
            print("lutfen giris yaparken 'quit' komutu dısında sayi kullaniniz.")
numbers.sort()
minnumbers=[]#ikinci en kucukleri tutacak
minn=numbers[0]#birinci en kuck sayi
birkere=True# n. kucuk sayi yapisi organizasyonu icin
for i in range(len(numbers)-1):
    if(numbers[i]>minn and birkere==True):
        minnumbers.append(numbers[i])
        birkere=False
    elif(birkere==False and numbers[i]==minnumbers[0]):
        minnumbers.append(numbers[i])
print("Ikinci en kucuk sayilar:\n",minnumbers)
