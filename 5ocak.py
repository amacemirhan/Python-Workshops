# -*- coding: utf-8 -*-
cumle=input("En az 5 harfli kelime veya cumle giriniz.")
cumle=cumle.lower
harfsayisi=len(cumle)
if (harfsayisi<5):
    print("Girilen ifade 5 harften az")
    exit()
cumleharf=list(cumle)
