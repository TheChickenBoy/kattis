e,f,p = map(int,input().split())
t = e+f
tot=0
re = 0
while t!=0:
    t+=re
    c = int(t/p)
    tot+= c
    
    re=t%p
    t=c
print(tot)
