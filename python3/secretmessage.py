from math import sqrt,ceil
for i in range(int(input())):
    l = input()
    k = ceil(sqrt(len(l)))
    l = l.ljust((k*k),'-')
    #print(k)
    s = ""
    o = []
    temp = []
    for j,c in enumerate(l):
        temp.append(c)
        if(j+1)%k == 0:
            o.append(temp)
            temp = []
    
    rotated = zip(*o[::-1])
    
    for r in rotated:
        #print("rad:",r)
        for c in r:
            if c == '-':
                continue
            s+=c

    print(s)
    
    # abc
    # def
    # ---
    # 
    # - d a
    # - e b
    # - f c
    # 
    # 
    # i l o v
    # e y o u
    # j a c k
    # - - - -
    # 
    # - j e i
    # - a y l
    # - c o o
    # - k u v 
    # 