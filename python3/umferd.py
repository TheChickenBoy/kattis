input()
total = 0
nr = 0
for i in range(int(input())):
    l = input()
    nr+=l.count('.')
    total+=len(l)
print(nr/total)