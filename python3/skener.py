n = list(map(int, input().split()))
f = []
for i in range(0,n[0]):
    l = input()
    for j in range(0,n[2]):
        f.append(l)
t = []
for i in range(0,len(f)):
    s=''
    for j, c in enumerate(f[i]):
        s += c*n[3]
    t.append(s)
for r in t:
    print(r)
