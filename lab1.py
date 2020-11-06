# Klavyeden 3 kenar uzunluğu girilen üçgenin türünü bulan
# programı yazınız
print("üçgenin üç adet kenar uzunluğunu giriniz:")
a=int(input("birinci kenar:"))
b=int(input("ikinci kenar:"))
c=int(input("üçüncü kenar:"))
if a==b and a==c:
    print("eşkenar üçgen")
elif a==b and a!=c:
    print("ikizkenar üçgen")
elif a==c and a!=b:
    print("ikizkenar üçgen")
elif b==c and a!=b:
    print("ikizkenar üçgen")
else:
    print("çeşitkenar üçgen")
    

