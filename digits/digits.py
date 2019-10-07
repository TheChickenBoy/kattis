import sys

def rek(tal,i):
    n = len(str(tal))
    if(int(tal)==1 and i != 1):
        return i
    else:
        return rek(n,i+1)

for l in sys.stdin:
    i = 0
    if 'END' in l:
        break
    elif int(l) == 1:
        print(1)
    else:
        n = len(l)-1
        print(rek(n,2))
