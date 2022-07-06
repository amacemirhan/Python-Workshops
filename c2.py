#C = 10
# n = 35
e = 7
n = 17 * 11
Fi= 16*10
# Fi(n) = (5-1) * (7-1) = 24
for d in range(10):
    if (e*d)%Fi==1:
        print("d values: ",d)
        break
#M = pow(C,d)%n
#print("M values: ",M)
M=88
C = pow(M,e)%n
print("C value: ",C)

print(pow(3,97)%353)
print(pow(3,233)%353)
print(pow(248,97)%353==pow(40,233)%353)
print(pow(248,97)%353)