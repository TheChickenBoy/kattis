l,x = map(int,input().split())
c=o=0
for i in range(0,x):
    q = input().split()
    if q[0] == 'enter':
        if c+int(q[1])<=l:
            c+=int(q[1])
        else:
            o+=1
    else:
        c-=int(q[1])
print(o)
