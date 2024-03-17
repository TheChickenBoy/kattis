for c in range(int(input())):
    l = input().split()
    x,y = map(int, l[1].split('/'))
    p = []
    while (x>1 or y>1):
        if x>y:
            p.append('r')
            x -= y
        else:
            p.append('l')
            y -= x
    n = 0
    for i in range(len(p) - 1, -1, -1):
        if p[i] == "r":
            n = (2 * (n + 1))
        else:
            n = (2 * n + 1)
    print(f"{l[0]} {n + 1}")