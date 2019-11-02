import sys
p,n = map(int,input().split())
d = {}
for i,l in enumerate(sys.stdin):
    if l in d:
        d[l]+=1
    else:
        d[l]=1
        if len(d) == p:
            print(i+1)
            exit()
print("paradox avoided")
