# -*- coding: utf-8 -*-
def nextDay(year,month,day):
    if(day==30):
        if(month==12):
            return year+1,1,1
        else:
            return year,month+1,1
    else:
        return year,month,day+1
def nextDayhicri(year,month,day):
    if(day==30):
        day=29
    if(day==29):
        if(month==12):
            return year+1,1,1
        else:
            return year,month+1,1
    else:
        return year,month,day+1
def isBayramdini(year,month,day):
    if(month==10 and day==1):#Ramazan bayrami
        return True
    elif(month==12 and day==10):#Kurban bayrami
        return True
    else:
        return False
def isBayram(year,month,day):
    if(month==4 and day==23):#23 nisan
        return True
    elif(month==5 and day==19):#19 mayıs
        return True
    elif(month==8 and day==30):#30 agustos
        return True
    elif(month==10 and day==29):#29 ekim
        return True
    elif(month==5 and day==1):#1 mayıs
        return True
    elif(month==7 and day==15):#15 temmuz
        return True
    else:
        return False
def isDateBefore(year1,month1,day1,year2,month2,day2):
    if(year1<year2):
        return True
    elif(year1==year2):
        if(month1<month2):
            return True
        elif(month1==month2):
            if(day1<day2):
                return True
            elif(day1==day2):
                print("Tarihler esit.")
                return False
    else:
        return False
def howManyBayram(year1,month1,day1,year2,month2,day2):
    counter=0
    counterh=0
    if(isDateBefore(year1, month1, day1, year2, month2, day2)==False):#birinci tarih ikinciden once degilse
        year1, month1, day1=year2, month2, day2#yerlerini degistir ki birinci ikinciden once olsun
    yearh=year1
    monthh=month1
    dayh=day1
    while(not(year1==year2 and month1==month2 and day1==day2)):#iki tarih de birbirine esit olmadigi surece devam eder
        if(isBayram(year1, month1, day1)):
            counter+=1
            year1, month1, day1=nextDay(year1, month1, day1)
        else:
            year1, month1, day1=nextDay(year1, month1, day1)
    while(not(yearh==year2 and monthh==month2 and dayh==day2)):#iki tarih de birbirine esit olmadigi surece devam eder
        if(isBayramdini(yearh, monthh, dayh)):
            counterh+=1
            yearh, monthh, dayh=nextDayhicri(yearh, monthh, dayh)
        else:
            yearh, monthh, dayh=nextDayhicri(yearh, monthh, dayh)
    print("İki tarih arasi dini bayramlarin sayisi:",counterh)
    print("İki tarih arasi milli bayramlarin sayisi:",counter)
    print("İki tarih arası gun sayisi:",counter+counterh)
howManyBayram(2001, 1, 1, 2001, 12, 29)
