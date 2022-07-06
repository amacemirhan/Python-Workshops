baslangicTl=4500
rechargeUsd= 97.77 + 215.71
bakiyeUsd=337.78
gun=0


from currency_converter import CurrencyConverter
c = CurrencyConverter()
dolar=c.convert(1, 'USD', 'TRY')
print("güncel dolar: ",dolar)

print("kesinti sonrası Usd, Tl: ",bakiyeUsd-(bakiyeUsd*5/100),(bakiyeUsd-(bakiyeUsd*5/100))*dolar)
print("tl olarak kar: ",((bakiyeUsd-(bakiyeUsd*5/100))*dolar)-baslangicTl)

while(bakiyeUsd<525):
    bakiyeUsd=bakiyeUsd+(bakiyeUsd*6/100)
    gun=gun+1
print(gun," gun sonra anaparayi cekecem")