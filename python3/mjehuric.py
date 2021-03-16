l = list(map(int, input().split()))
s = [1,2,3,4,5]
while True:
    if l[0] > l[1]:
        l[0], l[1], l[2], l[3], l[4] = l[1], l[0], l[2], l[3], l[4]
        print(*l)
    if l[1] > l[2]:
        l[0], l[1], l[2], l[3], l[4] = l[0], l[2], l[1], l[3], l[4]
        print(*l)
    if l[2] > l[3]:
        l[0], l[1], l[2], l[3], l[4] = l[0], l[1], l[3], l[2], l[4]
        print(*l)
    if l[3] > l[4]:
        l[0], l[1], l[2], l[3], l[4] = l[0], l[1], l[2], l[4], l[3]
        print(*l)
    if l == s:
        exit()
    