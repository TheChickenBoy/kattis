from math import sqrt,ceil
for i in range(int(input())):
    l = input()
    k = ceil(sqrt(len(l)))
    l = l.ljust((k*k),'-')
    s = ""
    #line2d = [line.split() for line in f]
    #print(k*k)
    for j,c in reversed(enumerate(l)):
        

    rotated = zip(*l[::-1])
    for r in rotated:
        print(r)
    # for r in rotated:
    #     for c in r:
    #         if c == '-':
    #             continue
    #         s+=c

    # print(s)
    