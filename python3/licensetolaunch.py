input()
n = list(map(int,input().split()))
t = 100001
d = 0
for i,v in enumerate(n):
    if v < t:
        t = v
        d = i
print(d)
