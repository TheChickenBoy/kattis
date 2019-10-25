aa = ['A','B','C','A','B','C','A','B','C','A','B','C']
ba = ['B','A','B','C','B','A','B','C','B','A','B','C']
ga = ['C','C','A','A','B','B','C','C','A','A','B','B']
ap = bp = gp = 0

n = int(input())
s = input()

for i,c in enumerate(s):
    if c == aa[i%12]:
        ap+=1
    if c == ba[i%12]:
        bp+=1
    if c == ga[i%12]:
        gp+=1

t = max(ap,bp,gp)
print(t)
if t == ap:
    print("Adrian")
if t == bp:
    print("Bruno")
if t == gp:
    print("Goran")
