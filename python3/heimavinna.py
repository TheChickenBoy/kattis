s = input()
s = s.split(';')
n=0
for e in s:
    if '-' in e:
        t = e.split('-')
        x = range(int(t[0]),int(t[1]))
        n+=len(x)+1
    else:
        n+=1
print(n)