import sys

input()
for l in sys.stdin:
    n=0
    l = l.split()
    l = list(map(int, l))
    tot = sum(l[1:l[0]+1])
    avg = tot/l[0]

    for i in range(1,l[0]+1):
        if l[i]>avg:
            n+=1
    print("%.3f" % ((n/l[0])*100)+'%')
