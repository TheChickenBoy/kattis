n,t = map(int,input().split())
a = list(map(int, input().split()))

if t == 1:
    print(7)
    exit()
elif t == 2:
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")
    exit()
elif t == 3:
    print(sorted(a[:3])[1])
    exit()
elif t == 4:
    print(sum(a))
    exit()
elif t == 5:
    s = 0
    for n in a:
        if n%2 == 0:
            s+=n
    print(s)
    exit()
elif t == 6:
    print(''.join(chr(97+i % 26) for i in a))
    exit()
elif t == 7:
    visited_index = [False]*n
    i = 0
    visited_index[i] = True
    while True:
        i = a[i]
        if i>=n:
            print("Out")
            exit()
        elif visited_index[i] == True:
            print("Cyclic")
            exit()
        elif i == n-1:
            print("Done")
            exit()
        visited_index[i] = True
        