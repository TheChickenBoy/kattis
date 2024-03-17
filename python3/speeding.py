from sys import stdin

n = stdin.readline()
ot = -1
od = -1
high = -1
for _ in range(int(n)):
    t,d = map(int, stdin.readline().split())
    q = (d-od)//(t-ot)
    if q > high:
        high = q
    ot = t
    od = d
print(high)