s = input().split()
dict={}
for w in s:
    if w in dict:
        dict[w]+=1
    else:
        dict[w]=1
dict = sorted(dict.values(),reverse=True)
if dict[0]==1:
    print("yes")
else:
    print("no")
