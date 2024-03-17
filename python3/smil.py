from sys import stdin

s = stdin.readline()

l = len(s)
i=0
while i<l:
    c = s[i]
    if c == ':' or c == ';':
        if s[i+1] == ')':
            print(i)
            i+=2
            continue
        elif s[i+1] == '-' and s[i+2] == ')':
            print(i)
            i+=3
            continue
        else:
            i+=1
            continue
    i+=1
