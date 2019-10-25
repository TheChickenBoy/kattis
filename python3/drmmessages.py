alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
l = input()

p1 = l[:len(l)//2]
p2 = l[len(l)//2:]

s1=""
s2=""
o = ""
t=t2 = 0
for i in range(len(p1)):
    t += alpha.index(p1[i])
    t2 += alpha.index(p2[i])
for i in range(len(p1)):
    s1 += alpha[(alpha.index(p1[i])+t)%26]
    s2 += alpha[(alpha.index(p2[i])+t2)%26]
for i in range(len(p1)):
    o+=alpha[(alpha.index(s1[i])+alpha.index(s2[i]))%26]
print(o)
