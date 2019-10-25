import sys
import math as m

for l in sys.stdin:
    dict = {}
    for c in l:
        if c in dict:
            dict[c]+=1
        else:
            dict[c]=1

    t = len(dict)-1
    print(m.factorial(t))
