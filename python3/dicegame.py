gunnar = list(map(int, input().split()))
emma = list(map(int, input().split()))
g1= []
g2= []
e1= []
e2= []


for i in range(gunnar[1]+1 - gunnar[0]):
    g1.append(gunnar[0]+i)
for i in range(gunnar[3]+1 - gunnar[2]):
    g2.append(gunnar[2]+i)
for i in range(emma[1]+1 - emma[0]):
    e1.append(emma[0]+i)
for i in range(emma[3]+1 - emma[2]):
    e2.append(emma[2]+i)
prob_g = prob_e = 0

if len(g1)%2 == 0:
    t1 = g1[int(len(g1)/2 - 1)]
    t2 = g1[int(len(g1)/2)]
    prob_g += (t1+t2)/2
else:
    prob_g += g1[int(len(g1)/2)]
if len(g2)%2 == 0:
    t1 = g2[int(len(g2)/2 - 1)]
    t2 = g2[int(len(g2)/2)]
    prob_g += (t1+t2)/2
else:
    prob_g += g2[int(len(g2)/2)]


if len(e1)%2 == 0:
    t1 = e1[int(len(e1)/2 - 1)]
    t2 = e1[int(len(e1)/2)]
    prob_e += (t1+t2)/2
else:
    prob_e += e1[int(len(e1)/2)]
if len(e2)%2 == 0:
    t1 = e2[int(len(e2)/2 - 1)]
    t2 = e2[int(len(e2)/2)]
    prob_e += (t1+t2)/2
else:
    prob_e += e2[int(len(e2)/2)]

if prob_e == prob_g:
    print("Tie")
elif prob_e > prob_g:
    print("Emma")
else:
    print("Gunnar")
