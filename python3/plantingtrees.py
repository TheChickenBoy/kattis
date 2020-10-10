tot = int(input())
d = list(map(int,input().split()))
d.sort(reverse=True)

days = d[0]
for i in range(1,len(d)):
    days -= 1
    days = max(days, d[i])

print(tot + days + 1)
