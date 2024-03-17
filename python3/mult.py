import sys

n = int(input())
m = int(input())
for l in sys.stdin:
    t = int(l)
    if t%m == 0:
        print(t)
        m = int(input())