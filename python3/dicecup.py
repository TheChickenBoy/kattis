from operator import itemgetter
n = input()
n = list(map(int, n.split()))
dict={}
for i in range(1,n[0]+1):
    for j in range(1,n[1]+1):
        if i+j in dict:
            dict[i+j]+=1
        else:
            dict[i+j]=1
dict = sorted(dict.items(),key=itemgetter(1),reverse=True)

h = dict[0][1]
for i in range(0,len(dict)):
    print(dict[i][0])
    if dict[i+1][1]<dict[i][1]:
        exit()
