num = list(map(int, input().split()))

l1 = list(range(num[0], num[1]))
l2 = list(range(num[1], num[2]))

while True:
    if l1 > l2:
        print(len(l1)-1)
        exit()
    else:
        print(len(l2)-1)
        exit()