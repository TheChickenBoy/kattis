import sys

time = 0
r = 0
dict = {}
for l in sys.stdin:
    l = l.split()
    if '-1' in l[0]:
        print(r,time)
        exit()
    if('right' in l[2]):
        if l[1] in dict:
            time+=int(l[0])+int(dict[l[1]])*20
            r+=1
        else:
            time+=int(l[0])
            r+=1
    else:
        if l[1] in dict:
            dict[l[1]]+=1
        else:
            dict[l[1]]=1
