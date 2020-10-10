r,n = input().split()
occupied = []
for i in range(int(n)):
    occupied.append(int(input()))
if r == n:
    print("too late")
for i in range(1,int(r)+1):
    if i not in occupied:
        print(i)
        exit()
