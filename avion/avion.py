import sys

i = 0
out = []
for l in sys.stdin:
    i+=1
    if 'FBI' in l:
        out.append(i)

if not out:
    print('HE GOT AWAY!')
else:
    print(*out)
