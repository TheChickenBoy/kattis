n = int(input())
tal = list(map(int,input().split()))
s = 0
for t in tal:
    if t < 0:
        s+=t*-1
print(s)
