w = int(input())
tot_a = 0
for i in range(int(input())):
    t1,t2 = map(int,input().split())
    tot_a+=(t1*t2)
print(int(tot_a/w))