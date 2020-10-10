from sys import stdin
for l in stdin:
    li = []
    if int(l) == 0:
        exit()
    for i in range(int(l)):
        li.append(input()) 
    li.sort(key = lambda x: x[:2])
    for n in li:
        print(n)