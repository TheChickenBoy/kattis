for i in range(int(input())):
    nrS = int(input())
    l = list(map(int, input().split()))
    l.sort()

    prev = dist = 0
    for s in l:
        if dist == 0:
            prev = s
            dist += s
        else:
            dist+=(s-prev)
            prev = s
    print(dist+l[-1]-2*l[0])