a = []
n = int(input())
v = input()
v = v.split()
v[0] = int(v[0])
v[1] = float(v[1])
t = 0
for i in range(1,n):
    v1 = input()
    v1 = v1.split()
    v1[0] = int(v1[0])
    v1[1] = float(v1[1])

    t+= (v[1]+v1[1])/2 * (v1[0]-v[0])
    v = v1
print(t/1000)
