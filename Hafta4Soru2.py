# -*- coding: utf-8 -*-
devam="E"
def IntToChar(num):
    switcher2={
        0:"a",
        1:"b",
        2:"c",
        3:"d",
        4:"e",
        5:"f",
        6:"g",
        7:"h",
        8:"i",
        9:"j",
        10:"k",
        11:"l",
        12:"m",
        13:"n",
        14:"o",
        15:"p",
        16:"q",
        17:"r",
        18:"s",
        19:"t",
        20:"u",
        21:"v",
        22:"w",
        23:"x",
        24:"y",
        25:"z",
        26:"A",
        27:"B",
        28:"C",
        29:"D",
        30:"E",
        31:"F",
        32:"G",
        33:"H",
        34:"I",
        35:"J",
        36:"K",
        37:"L",
        38:"M",
        39:"N",
        40:"O",
        41:"P",
        42:"Q",
        43:"R",
        44:"S",
        45:"T",
        46:"U",
        47:"V",
        48:"W",
        49:"X",
        50:"Y",
        61:"Z",
        }
    return switcher2.get(num,"Deger disina ciktiniz!")
def CharToInt(arg):
    switcher={
        "a":0,
        "b":1,
        "c":2,
        "d":3,
        "e":4,
        "f":5,
        "g":6,
        "h":7,
        "i":8,
        "j":9,
        "k":10,
        "l":11,
        "m":12,
        "n":13,
        "o":14,
        "p":15,
        "q":16,
        "r":17,
        "s":18,
        "t":19,
        "u":20,
        "v":21,
        "w":22,
        "x":23,
        "y":24,
        "z":25,
        "A":26,
        "B":27,
        "C":28,
        "D":29,
        "E":30,
        "F":31,
        "G":32,
        "H":33,
        "I":34,
        "J":35,
        "K":36,
        "L":37,
        "M":38,
        "N":39,
        "O":40,
        "P":41,
        "Q":42,
        "R":43,
        "S":44,
        "T":45,
        "U":46,
        "V":47,
        "W":48,
        "X":49,
        "Y":50,
        "Z":61,
        }
    return switcher.get(arg,"Deger disina ciktiniz!")
def myLen(string):#Hazir fonksiyon kullanmamak icin kendi len fonksiyonum
    i=0
    for s in string:
        i+=1
    return i
while(devam=="E" or devam=="e"):
    tercih=input("Yazmak icin Y cozmek icin C ye basiniz:")
    sayi=int(input("Anahtar sayi giriniz:"))
    mesaj=input("Mesaj giriniz:")
    print("Yeni mesaj:",end="")
    if(tercih=="C" or tercih=="c"):#cozmek icin ise eksiyle carpiyorum ki cıkartma yapsin sola kaysin
        sayi*=-1
    for i in range(myLen(mesaj)):
        print(IntToChar(CharToInt(mesaj[i])+sayi),end="")#once karakteri sayiya cevirir sonra ekleme veya cikarma yapip tekrar karaktere cevirir 
    devam=input("Devam etmek istiyor musunuz(E/H):")

