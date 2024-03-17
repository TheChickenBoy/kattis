n = input()
l = list(map(int, input().split()))

s = list(set(l))
nl = []
high = 0
for c in s:
    if c > high and l.count(c) == 1:
        high = c
        index = l.index(c)
    l = [x if x!=c else 0 for x in l]
try:
    print(index+1)
except:
    print("none")