iq = {}
x = input()
l = input().split()

for j,p in enumerate(l):
    iq[j+2] = int(p)

q = {k: v for k, v in sorted(iq.items(), key=lambda item: item[1])}
s = "1 "
for key in q:
    s+=str(key)+" "
print(s)