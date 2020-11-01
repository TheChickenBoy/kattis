d ={}
l = input()

for c in l:
    if c in d:
        d[c]+=1
    else:
        d[c] = 1

s = input()
count = 0
target = len(l)
n = 0
for c in s:
    if c in d:
        n+=d[c]
    else:
        count += 1
    
    if n == target:
        print("WIN")
        exit()
    elif count == 10:
        print("LOSE")
        exit()