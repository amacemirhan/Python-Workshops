C = 10
n = 35
e = 5
# n = 5 * 7
# Fi(n) = (5-1) * (7-1) = 24
for d in range(10):
    if (e*d)%24==1:
        print("d values: ",d)
        break
M = pow(C,d)%n
print("M values: ",M)