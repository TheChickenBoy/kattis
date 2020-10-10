l = list(map(int, input().split()))
tasks = list(map(int, input().split()))

for i, t in enumerate(tasks):
    l[1]-=t
    if l[1]<0:
        print(i)
        exit()
    elif l[1] == 0:
        print(i+1)
        exit()
print(i+1)