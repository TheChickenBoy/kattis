d={}
for _ in range(int(input())):
    l = input().split()
    if l[2] in d:
        if int(l[1]) > d[l[2]][1]:
            d[l[2]] = l[0], int(l[1])
    else:
        d[l[2]] = l[0], int(l[1])

print(len(d))
for i in sorted(d.values()):
    print(i[0])