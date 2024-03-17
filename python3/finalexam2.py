from sys import stdin

n = stdin.readline()
l = []
for _ in range(int(n)):
    l.append(input())
l2 = l.copy()
l.pop(0)
r = 0
for i in range(len(l)):
    if l[i] == l2[i]:
        r+=1
print(r)
