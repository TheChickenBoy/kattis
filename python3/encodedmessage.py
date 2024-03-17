from math import sqrt
for i in range(int(input())):
    l = input()
    x = int(sqrt(len(l)))
    count = x-1
    ind = x-1
    o=""
    for j in range(len(l)):
        c = l[ind]
        o+=c
        if ind + x > (x*x)-1:
            count-=1
            ind=count
        else:
            ind += x
    print(o)