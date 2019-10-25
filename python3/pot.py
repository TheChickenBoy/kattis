x = 0
for i in range(0,int(input())):
    n = int(input())
    x+=(n//10)**(n%10)
print(x)
