time = 210
bp = int(input())
for _ in range(int(input())):
    l = input().split()
    time -= int(l[0])
    if time < 0:
        print(bp)
        exit()
    else:
        if l[1] == 'T':
            bp+=1
            if bp>8:
                bp = 1