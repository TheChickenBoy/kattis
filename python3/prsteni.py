n = int(input())
tal = list(map(int,input().split()))
for i in range(n-1):
    c = 1
    while ((tal[0]*c)%(tal[i+1])) != 0:
        c+=1
    print(str(int((tal[0]*c)/(tal[i+1])))+'/'+str(c))
