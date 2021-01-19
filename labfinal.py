# -*- coding: utf-8 -*-
giris=""
words=[]
while(giris!="quit"):
    giris=input("")
    if(giris!="quit"):
        words.append(giris)
print("-------------------------------")
for i in range(len(words)):
    print(words[len(words)-i-1])
    