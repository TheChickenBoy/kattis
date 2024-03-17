p,t = map(int,input().split())
r=0
q = 0
for _ in range(p):
    for _ in range(t):
        s = input()
        if s[1:].islower():
            q+=1
    if q==t:
        r+=1
    q=0
print(r)