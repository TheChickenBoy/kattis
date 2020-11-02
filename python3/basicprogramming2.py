from collections import Counter
from math import ceil
n,t = map(int,input().split())
a = list(map(int, input().split()))

if t == 1:
    front_i = 0
    back_i = n-1
    a.sort()

    while front_i < back_i:
        if a[front_i] != a[back_i] and a[front_i] + a[back_i] == 7777:
            print("Yes")
            exit()
        elif a[front_i] + a[back_i] < 7777:
            front_i+=1
        else:
            back_i-=1
    print("No")
    exit()
elif t == 2:
    counter = Counter(a) 
    for values in counter.values():
        if values > 1: 
            print("Contains duplicate")
            exit()
    print("Unique")
    exit()
elif t == 3:
    counter = Counter(a) 
    for key in counter.keys():
        if counter[key] > (n/2): 
            print(key)
            exit()
    print(-1)
    exit()
elif t == 4:
    a.sort()
    if n%2 == 0:
        #print(n/2)
        print(f"{a[int((n/2))-1]} {a[int((n/2))]}")
    else:
        print(f"{a[int((n/2))]}")
    exit()
elif t == 5:
    r = [x for x in a if 100 <= x <= 999]
    r.sort()
    print(*r)
    exit()
        