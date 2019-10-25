import sys
for l in sys.stdin:
    #l = int(l)
    l = l.strip()
    if l == '0':
        exit()
    t = 0
    for c in l:
        t+=int(c)
    i=11
    while True:
        x = str(int(l)*i)
        r = 0
        for c in x:
            r+=int(c)
        if r == t:
            print(i)
            break
        i+=1
