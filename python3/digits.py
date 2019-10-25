import sys

for l in sys.stdin:
    i = 0
    if 'END' in l:
        break
    if len(l)==2:
        if int(l) == 1:
            print(1)
        else:
            print(2)
    elif len(l) >= 3 and len(l)<=11:
        print(3)
    else:
        print(4)
