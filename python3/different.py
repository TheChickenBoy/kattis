import sys

for l in sys.stdin:
    l = l.split()
    if int(l[0])>int(l[1]):
        print(int(l[0])-int(l[1]))
    else:
        print(int(l[1])-int(l[0]))
