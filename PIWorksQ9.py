# PIWorks question 9
# Mehmed Emirhan Amaç
# emirhan_amac01@hotmail.com
def isDivisible(a):
    b=str(a)
    top=0
    for i in b:
        top+=int(i)
    if(a % top):
        return False
    else:
        return True
print(isDivisible(75))
print(isDivisible(171))
print(isDivisible(481))

'''
OUTPUT
False
True
True
'''
