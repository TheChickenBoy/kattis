l = list(map(int,input().split()))
print(max(l[0]-l[1],l[1])*max(l[0]-l[2],l[2])*4)