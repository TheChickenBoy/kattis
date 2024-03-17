for _ in range(int(input())):
    a = list(map(int, input().split()))
    t = 0
    b = 0
    for i in a:
        if i == 1:
            t = i
        else:
            if i > t*2:
                b += i - t*2
            t = i
    print(b)