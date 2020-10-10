from sys import stdin
for i, line in enumerate(stdin):
    l = list(map(int, line.split()))
    del l[0]
    l.sort()
    print(f"Case {i+1}: {l[0]} {l[-1]} {l[-1]-l[0]}")
