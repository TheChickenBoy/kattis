winners = {}
x = 0
for i in range(0,int(input())):
    l = input().split()
    if x == 12:
        exit()
    if l[0] in winners:
        continue
    else:
        winners[l[0]]=l[1]
        print(l[0],l[1])
        x+=1
