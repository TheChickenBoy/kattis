d = 0
dict = {}
for i in range(0,int(input())):
    l = list(map(int,input().split()))
    for j in range(l[0],l[1]+1):
        if j not in dict:
            dict[j] = 1
            d+=1
print(len(dict))
