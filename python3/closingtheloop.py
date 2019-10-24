for i in range(0,int(input())):
    n = int(input())
    nrB = nrR = 0
    Blist = []
    Rlist = []
    ropes = input().split()
    for c in ropes:
        if 'R' in c:
            nrR +=1
            Rlist.append(c)
        elif 'B' in c:
            nrB +=1
            Blist.append(c)

    sorted(Rlist, reverse = True)
    sorted(Blist, reverse = True)
    x = min(len(Rlist),len(Blist))
    s = 0
    for i in range(0,x):
        s+=int(Rlist[i][0])
        s+=int(Blist[i][0])
    print(s-x)



"""
6R 1B 7R 3B

6+1+7+3 = 10+7 |= 17-4 = 13

5+5 = 10
"""
