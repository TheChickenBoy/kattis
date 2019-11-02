import sys, bisect

for l in sys.stdin:
    if int(l) == 0:
        exit()

    l1 = []
    l1s = []
    l2 = []
    for i in range(int(l)*2):
        t = int(input())
        if i < int(l):
            l1.append(t)
            bisect.insort(l1s,t)
        else:
            l2.append(t)
    l2.sort()
    for q in l1:
        print(l2[l1s.index(q)])
    print()
