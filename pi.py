n=60
top=0.0
sign=True
for i in range(1,n):
    if n%2:
        print(n)
        if sign:
            top+=1/i
            sign=False
        else:
            top-=1/i
            sign=True
pi=top*4
print(pi)