for i in range(0,int(input())):
    n = int(input())
    l = input().split()
    dict={}
    for g in l:
        if g in dict:
            dict[g]+=1
        else:
            dict[g]=1
    dict = sorted(dict,key=dict.get)
    print("Case #"+str(i+1)+": "+dict[0])
