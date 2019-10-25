import sys
from math import floor

for l in sys.stdin:
    if "0 0" in l:
        exit()
    i = list(map(int,l.split()))
    t = i[0]%i[1]
    print(str(floor(i[0]/i[1]))+ " " + str(t) + " / "+str(i[1]))
