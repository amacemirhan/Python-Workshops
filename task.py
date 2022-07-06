import sympy as sy
import numpy as np
import string

inputstr = """
1
8 4
2 6 9
8 5 9 3
"""
maxi = 0
summary=0
lastb=0
s = inputstr.splitlines()
for i in range(len(s)):
    s[i] = s[i].split()

for a in range(0,len(s)):
    for b in range(lastb+1,len(s[a])):
        if b==lastb or b==lastb-1 or b==lastb+1:
            try:
                number_list = [int(s[a][b - 1]), int(s[a][b]), int(s[a][b + 1])]
            except IndexError:
                try:
                    number_list = [0, int(s[a][b]), int(s[a][b + 1])]
                except IndexError:
                    number_list = [int(s[a][b - 1]), int(s[a][b]), 0]
            while True:
                max_value = max(number_list)
                max_index = number_list.index(max_value)
                if(not sy.isprime(max_value)):
                    summary += max_value
                    lastb=b + max_index - 1
                    print(max_value)
                    break
                else:
                    number_list[max_index] = 0
            break



    if(summary>maxi):
        maxi=summary
        summary=0

print(maxi)