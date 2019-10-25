dict={}
for i in range(0,int(input())):
    l = input().split()
    if l[0].isdigit():
        dict[l[1]] = int(l[0])/2
    else:
        dict[l[0]] = int(l[1])
dict = sorted(dict,key=dict.get)
for c in dict:
    print(c)
