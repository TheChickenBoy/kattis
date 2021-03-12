for x in range(int(input())):
    l = list(map(int,input().split()))
    for i,e in enumerate(l[1:],start=1):
        if e+1 == l[i+1]:
            continue
        else:
            print(i+1)
            break