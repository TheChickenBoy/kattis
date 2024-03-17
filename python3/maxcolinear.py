from math import atan, pi
from collections import Counter
from sys import stdin, stdout

def check_point(p, m):
    angles = []

    for q in m:
        if p == q:
            continue
        if (q[0] - p[0]) == 0:
            angles.append(atan(
                pi/2
            ))
        else:
            angles.append(atan(
                (q[1] - p[1]) / (q[0] - p[0])
            ))
    angles.sort()

    occurence_count = Counter(angles)
    return occurence_count.most_common(1)[0][1]

line = stdin.readline()
while line:
    if line == "0\n":
        exit()
    m = []
    for _ in range(int(line)):
        line = stdin.readline()
        x,y = map(int,line.split())
        m.append((x,y))
    
    h = -1
    if len(m) > 1:
        for p in m:
            h = max(h,check_point(p,m))
        stdout.write(str(h+1))
        stdout.write("\n")
    else:
        stdout.write("1\n")
    line = stdin.readline()
