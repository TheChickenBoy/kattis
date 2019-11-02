for q in range(0,int(input())):
    n = int(input())
    Blist, Rlist = [], []
    for c in input().split():
        if 'R' in c:
            Rlist.append(int(c[:-1]))
        elif 'B' in c:
            Blist.append(int(c[:-1]))

    Rlist = sorted(Rlist, reverse = True)
    Blist = sorted(Blist, reverse = True)
    x = min(len(Rlist),len(Blist))
    if x == 0:
        print("Case #"+str(q+1)+": " + "0")
        continue
    r = sum(Rlist[:x]) + sum(Blist[:x]) - x*2

    print("Case #"+str(q+1)+": " + str(int(r)))
