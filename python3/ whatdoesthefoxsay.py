for i in range(int(input())):
    l = input().split()
    noice = []
    while True:
        s = input()
        if s == "what does the fox say?":
            break
        noice.append((s.split())[2])
    print(*[x for x in l if x not in noice])