# -*- coding: utf-8 
sozluk={}
cvp=input("Sozluge yeni kayit eklemek istiyor musunuz?[E/H]")
cvp=cvp.upper()
while(cvp=="E"):
    if(cvp=="E"):
        key=input("Ogrenci no:")
        value=input("Ogrenci ad:")
        sozluk[key]={value}
    cvp=input("Sozluge yeni kayit eklemek istiyor musunuz?[E/H]")
    cvp=cvp.upper()
print(sozluk.items())
