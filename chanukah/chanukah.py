for i in range(int(input())):
    l = list(map(int,input().split()))

    c = 0
    for j in range(1,l[1]+1):
        c+=j
    print(l[0],c+l[1])